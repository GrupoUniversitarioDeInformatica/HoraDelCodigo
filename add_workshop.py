"""
Use this script to add new workshops to this repo.

This script will create the new workshop README.md for you in the right path to keep it organised
and will update the README.md on the root of this repo to display a tidy Table of Contents grouped by year.
"""

import argparse
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

workshops_dir = Path(__file__).parent / "workshops"


def _clean_string(string: str) -> str:
    string = re.sub(r"[^A-Za-z0-9\'\-]", "-", string.replace(" ", "_").lower())
    return re.sub(r"-+", "-", string).strip("-") or "-"


def _setup_new_workshop_dir(topic: str, workshop_name: str, author: str):
    workshops_dir.mkdir(exist_ok=True)

    topic_dir = workshops_dir / _clean_string(topic)
    topic_dir.mkdir(exist_ok=True)

    total_workshops_for_topic = len(list(topic_dir.iterdir()))

    now = datetime.now()

    new_workshop_dir = (
        workshops_dir
        / _clean_string(topic)
        / f"{total_workshops_for_topic:03}_{_clean_string(workshop_name)}_{now.strftime('%Y%m%d')}"
    )

    new_workshop_dir.mkdir()

    readme_md = new_workshop_dir / "README.md"
    readme_md.write_text(f"""\
# {topic.upper()} - {workshop_name}

- Autor: {author}
- Fecha de adición: {now.strftime("%Y-%m-%d %H:%M:%S")}

---

## Descripción

Este taller va de...

## Requisitos

Se recomienda a los participantes que:

- ...

## Otros detalles

Para el que quiera dar este taller, recomiendo que...
""")


def _generate_root_readme_md() -> None:
    README_ROOT_CONTENTS = """\
# HoraDelCodigo

> [!IMPORTANT]
> Do not edit this README.md file manually, instead use the [add_workshop.py](add_workshop.py) script please.
>
> No editéis este fichero README.md manualmente, en su lugar utilizad el script [add_workshop.py](add_workshop.py).

---

## Tabla de Contenidos
"""

    workshops_per_year: dict[int, dict[str, list[tuple[str, str]]]] = defaultdict(dict)

    for topic_dir in workshops_dir.iterdir():
        for workshop_dir in topic_dir.iterdir():
            match = re.match(r"^\d{3}_(?P<workshop_name>.*)_(?P<year>\d{4})\d{4}$", workshop_dir.name)
            if not match:
                raise RuntimeError("Could not get info from workshop dir name")

            workshop_name, year = match.groups()

            workshop_name = workshop_name.capitalize().replace("-", " ")
            year = int(year)

            workshops = workshops_per_year[year].get(topic_dir.name, [])
            workshops.append(
                (
                    workshop_name,
                    str(workshop_dir.relative_to(workshops_dir.parent)),
                )
            )
            workshops_per_year[int(year)][topic_dir.name] = workshops

    with (workshops_dir.parent / "README.md").open("wt") as f:
        f.write(README_ROOT_CONTENTS)

        for year, workshops_by_topic in workshops_per_year.items():
            lines = [f"### {year}"]
            for topic, workshops in workshops_by_topic.items():
                lines.append(f"**{topic.capitalize()}**")
                for workshop_name, workshop_path in workshops:
                    lines.append(f"- [{workshop_name}]({workshop_path})")
            f.write("\n" + "\n".join(lines))


parser = argparse.ArgumentParser()

parser.add_argument(
    "-t",
    "--topic",
    required=True,
    help="The topic of the workshop in 1 word. Ex: neovim, python, java, latex,...",
)
parser.add_argument(
    "-wn",
    "--workshop-name",
    required=True,
    help="The name of the workshop (in quotes please). Ex: 'From zero to hero', 'how not to suck at latex',...",
)
parser.add_argument(
    "-a",
    "--author",
    required=True,
    help="Your name (in quotes please). Ex: 'Perico de los Palotes', 'Linus Torvalds', 'Bill Puertas',...",
)

try:
    args = parser.parse_args()
except:  # noqa: E722
    parser.print_help()
    raise

_setup_new_workshop_dir(args.topic, args.workshop_name, args.author)
_generate_root_readme_md()
