---
theme: default
background: https://imgs.search.brave.com/Bre3iPYLA8ZamjTo_FX5dX6WSIZkGqAxM1NOrdJI25Q/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzE1LzkxLzc4LzA0/LzM2MF9GXzE1OTE3/ODA0MjJfMHp1R0VI/ZmZYQVd6ekJwR3RJ/M1dwUG95TkhaTU1m/M1kuanBn
title: Taller de Desarrollo Full Stack
author: Miguel Ángel Martín López [@miguelachaotic](https://github.com/miguelachaotic)
keywords: gui,python,node,vue,uva
info: |
  ## Taller de desarrollo web Full Stack

  Escrito en Markdown y presentado via [Sli.dev](https://sli.dev)
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Taller de desarrollo Full Stack

<p class="text-2xl text-white text-shadow-md">
Miguel Ángel Martín López <a href="https://github.com/miguelachaotic" target="_blank">@miguelachaotic</a>
</p>

## GUI - Grupo Universitario de Informática

## Escuela de Ingeniería Informática UVa

---
layout: center
zoom: 0.8
---

# Tabla de contenidos

<Toc text-sm minDepth="1" maxDepth="2" columns="2" class="space-x-10"/>

---
transition: fade-out
layout: quote
---

# ¿Qué significa Full Stack?

<v-clicks>

- Desarrollo web a todos los niveles: Interfaz, comunicación, modelo e integridad de información.
- Combinación de varios niveles de organización: FrontEnd, BackEnd, Bases de Datos, etc...
- Con lo que se impartirá en este taller podréis construir una aplicación web básica, pero funcional.

</v-clicks>

<v-clicks> <br> </v-clicks>

<v-after>

### Es importante saber la diferencia entre Página Web y Aplicación Web

</v-after>


---
transition: slide-left
level: 2
layout: image-right
image: https://imgs.search.brave.com/L5X_0bqvf9kiJxiBBt7OEKBdEttE1kN3by3DNuM2k6c/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTg1/NDM3NTg3NS9waG90/by9uZW9uLWh0dHAt/aW50ZXJuZXQtY29u/bmVjdGlvbi1wcm90/b2NvbC1zaWduLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1Q/UE9aeFdYYUl2dUhV/a0pwWHpWNlV6dTZr/VjdKMUlqdlBkNWRm/OHRSLUdrPQ
backgroundSize: 80% 40%
---

# Protocolo HTTP

HyperText Transfer Protocol

<v-clicks>

- Protocolo usado por aproximadamente el 98% de las aplicaciones web (La mayoría en su versión segura `HTTPS`)
- Las aplicaciones necesitan un **servidor** para funcionar. Para este taller, el servidor será nuestro PC / portátil.
- Dentro de la misma red, podremos acceder a las aplicaciones diseñadas por los demás asistentes.

</v-clicks>

---
transition: slide-left
level: 2
---

# BackEnd
Será la primera parte del taller. Nos enfocaremos en crear una **API REST** usando una librería en Python llamada **[FastAPI](https://fastapi.tiangolo.com/)**.

<v-click>

## ¿Cómo funciona?
````md magic-move {lines: true}
```py [FastAPI] {*|1-3|4|5-8|*}
@app.get(
  '/items/{item_id}'
)
async def get_item(item_id: Annotated[int, Path(gt=0)]):
  return {
    "status": "ok",
    "id": item_id
  }
```
````
</v-click>
<v-click>
Para obtener el objeto tendríamos que hacer una petición "GET /items/4" y devolvería el siguiente JSON:
</v-click>
<v-click>
````md magic-move
```json
{"status": "ok", "id": 4}
```
```json
{
  "status": "ok",
  "id": 4
}
// Más habitual en este formato
```
````
</v-click>


---
transition: slide-left
level: 2
---

# FrontEnd
Será la segunda parte del taller. Usaremos la API creada en la primera parte para crear una interfaz de usuario que interactúe con nuestro dominio. Para desarrollarlo usaremos 2 tecnologías clave: [Vue](https://vuejs.org/) y [TailwindCSS](https://tailwindcss.com/).

````md magic-move
```html
<!-- Incrementar un contador al pulsar un botón -->
<button id="counter-btn">0</button>
<script>
  let counter = 0;
  const button = document.getElementById('counter-btn');
  function render() {
    button.textContent = counter;
  }
  button.addEventListener('click', () => {
    counter++;
    render();
  });
  render();
</script>
```
```vue
<!-- Código en Vue -->
<template>
  <!-- Cuando se hace click en el boton se incrementa counter y se renderiza -->
  <!-- Lo que hay en el atributo `class` es TailwindCSS. Podemos usar estilos sin definirlos manualmente -->
  <button @click="counter++" 
    class="px-3 py-2 bg-blue-400 hover:bg-blue-500 rounded-lg"
  >{{ counter }}</button> 
</template>

<script setup>
import { ref } from 'vue';

const counter = ref(0);
</script>
```
````
<div v-if="$route.query.clicks === undefined">Un poco díficil de entender. No es nada escalable para proyectos grandes.</div>
<v-click>
Vue simplifica mucho las cosas! Es un poco enrevesado al principio, pero muy útil para desarrollar de forma eficiente y rápida!
</v-click>


---
transition: slide-up
level: 2
---

# Servidor Web

Para ejecutar nuestra aplicación web, necesitamos un **servidor web**, que es aquel que recibe las peticiones y responde acorde a la petición que realicemos.

<v-click>

Usaremos una tecnología llamada **[NGINX](https://nginx.org/)**. NGINX es un servidor web que permite redirigir peticiones en base a diversos criterios. Para facilitar las cosas, únicamente haremos dos cosas con esta tecnología:

</v-click>

<v-clicks>

- Redirigir peticiones en base a URL
- Implementar HTTPS mediante certificados autofirmados.

</v-clicks>


<v-click>


```sh [generar_certificados]
# Como generar certificados para HTTPS
mkdir -p ./certs # creamos la carpeta certs si no estaba creada antes
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout nginx/certs/selfsigned.key \
  -out nginx/certs/selfsigned.crt \
  -subj "/C=ES/ST=Valladolid/L=Valladolid/O=LocalDev/OU=Dev/CN=localhost"

```

En el fichero `nginx/default.conf` podréis ver cómo se configura NGINX. No es parte de este taller explicar cómo funciona, lo importante es saber que redirige a los servicios que nos interesa.

</v-click>

---
layout: default
level: 1
---

# Desarrollo Backend

## Bases de Datos
Usaremos una base de datos relacional llamada *MariaDB*. Está basada en **SQL**. 

<v-click>
No desarrollaremos la base de datos como tal, vamos a partir de un ejemplo.

El ejemplo que he propuesto es un foro donde hay usuarios, posts y comentarios. Se establecen relaciones entre los datos, en concreto las siguientes:
</v-click>

<v-clicks>

- Los usuarios pueden tener 0 o más posts.
- Cada post puede tener 0 o más comentarios.
- Cada usuario puede comentar 0 o más veces en un post.

</v-clicks>

<v-click>

¿Pueden existir usuarios sin posts que hayan comentado en otros posts?
</v-click>


<v-click>

En resumen, sí. Habrá que buscar una forma de tratar con estos datos de una forma eficiente.
</v-click>


---
transition: slide-up
level: 2
---

# SQLAlchemy

Para conectarnos a la base de datos usaremos una librería **ORM** que nos evitará los problemas de realizar consultas SQL. (ORM = Object Relational Mapping).

````md magic-move {lines: true}
```python {*|7-10|12|14|16-21|*}
# Fichero database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

DB_USER = "app_user"
DB_PORT = 3306
# completad obteniendo las variables del entorno usando la siguiente linea
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session]:
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
```
````

---
level: 3
---

### Haciendo consultas con SQLAlchemy

Hasta ahora lo que hemos conseguido es conectarnos, pero no podemos acceder a esa información. <p v-if="Number($route.query.clicks ?? 0) <= 5">Ahora vamos a crear una serie de modelos que representan las tablas existentes en la base de datos:</p><p v-else>Y podemos usar ese modelo para realizar consultas a la base de datos</p>

<div class="grid grid-cols-1">

````md magic-move {lines: true}
```python {*|6|7|8-12|14-15|*}
# models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  email = Column(String(150), nullable=False, unique=True, index=True)
  password_hash = Column(String(255), nullable=False)
  created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

  posts = relationship("Post", back_populates="author", cascade="all, delete")
  comments = relationship("Comment", back_populates="author", cascade="all, delete")
```
```python {*|4|3-6|7-10|9|11|12,13|14|*}
from models import User
from schemas import OutUser # Ahora veremos esto
@app.get(
  '/users/{user_id}',
  response_model=OutUser
)
async def get_user(
  user_id: Annotated[int, Path(gt=0)],
  session: Depends(get_db)
):
  db_user = session.query(User).filter(User.id == user_id).first()
  if db_user is None:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return db_user
```
````

</div>


---
level: 2
---

# FastAPI
Como se dijo antes, **FastAPI** es una librería para la creación de APIs REST. (REST = Representational State Transfer). Este tipo de APIs se caracterizan por la ausencia de estado, es decir, que por defecto no existe un mecanismo que mantenga estado entre cliente y servidor.

<v-click>

````md magic-move {lines: true}
```py {*|9}
from fastapi import FastAPI

# con esto creamos la aplicación
app = FastAPI( 
  title="Mi primera API",
  root_path='/api' # ya veremos por qué esto es importante
)

@app.get('/hola-mundo')
async def get_hola_mundo():
  return {'msg': 'Hola Mundo!'}
```
```py {9-15|*}
from fastapi import FastAPI

# con esto creamos la aplicación
app = FastAPI( 
  title="Mi primera API",
  root_path='/api' # ya veremos por qué esto es importante
)

@app.get(
  '/hola-mundo',
  response_model=dict[str, str],
  name="Hola Mundo",
  operation_id="hola_mundo",
  description="Devuelve un diccionario con un mensaje Hola Mundo"
)
async def get_hola_mundo():
  return {'msg': 'Hola Mundo!'}
```
```py 
from fastapi import FastAPI

# con esto creamos la aplicación
app = FastAPI( 
  title="Mi primera API",
  root_path='/api' # ya veremos por qué esto es importante
)

@app.get('/hola-mundo')
async def get_hola_mundo():
  return {'msg': 'Hola Mundo!'}
```
````
<v-click>

En FastAPI rara vez es necesario documentar, porque la propia documentación se hace en el código. Luego, en la parte del FrontEnd veremos porqué es importante todos esos parámetros en los decoradores (el `@app.get(...)`).

</v-click>

</v-click>


---
level: 2
---

# Modelos de datos: Pydantic
Para cada llamada de la API, hay que definir un modelo de datos de entrada o salida. Para hacerlo usaremos una librería de validación de tipos llamada **Pydantic**. **MUY IMPORTANTE**: Los nombres de los atributos deben coincidir con el modelo de SQLAlchemy. Un ejemplo para usuarios:
````md magic-move 
```py
class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  email = Column(String(150), nullable=False, unique=True, index=True)
  password_hash = Column(String(255), nullable=False)
  created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

  posts = relationship("Post", back_populates="author", cascade="all, delete")
  comments = relationship("Comment", back_populates="author", cascade="all, delete")
```
```py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
  name: str
  email: EmailStr

class UserCreate(UserBase):
  password: str

class UserUpdate(BaseModel):
  name: str | None = None
  email: EmailStr | None = None

class UserOut(UserBase):
  id: int
  created_at: datetime

  class Config:
    from_attributes = True # esto habilita el modo ORM
```
```py
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
  name: str
  email: EmailStr

class UserCreate(UserBase):
  password: str

class UserUpdate(BaseModel):
  name: str | None = None
  email: EmailStr | None = None

class UserOut(UserBase):
  model_config = ConfigDict(from_attributes=True) # otra alternativa para ORM

  id: int
  created_at: datetime
```
````


---
layout: cover
level: 2
---

# Distintos tipos de peticiones y Dependencias

---
zoom: 0.8
transition: fade
level: 3
---

## GET

Una petición GET representa una petición por parte del usuario para obtener un recurso o servicio de nuestra API. 

Por ejemplo, `GET /posts/14`, Obtiene el post con el ID 14.

```py
from fastapi import Depends, HTTPException, status
from database import get_db
from models import Post
from schemas import PostOut

@app.get(
  '/posts/{post_id}',
  response_model=PostOut
)
async def get_post(
  post_id: int,
  session: Depends(get_db)
):
  db_post = session.query(Post).filter(Post.id == post_id).first()
  if db_post is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Post con id={post_id} no encontrado."
    )
  return db_post
```
---
zoom: 0.8
transition: fade
level: 3
---

## POST

Una petición POST se utiliza para crear un nuevo recurso en el servidor.

Por ejemplo, `POST /posts` crea un nuevo post a partir del *cuerpo* o *body* de la petición.

El cuerpo es un único modelo de datos que no aparece en la ruta.

```py
from schemas import PostCreate

@app.post(
  '/posts',
  response_model=PostOut,
  status_code=status.HTTP_201_CREATED
)
async def create_post(
  post: PostCreate,
  session: Depends(get_db)
):
  db_post = Post(**post.dict())
  session.add(db_post)
  session.commit()
  session.refresh(db_post)
  return db_post
```

---
zoom: 0.8
transition: fade
level: 3
---

## PUT

Una petición PUT se usa para reemplazar completamente un recurso existente.

Por ejemplo, `PUT /posts/14` reemplaza el post con ID 14 con los nuevos datos enviados en el body.

```py
@app.put(
  '/posts/{post_id}',
  response_model=PostOut
)
async def update_post(
  post_id: int,
  updated_post: PostCreate,
  session: Depends(get_db)
):
  db_post = session.query(Post).filter(Post.id == post_id).first()
  if db_post is None:
    raise HTTPException(status_code=404, detail="Post no encontrado")
  for key, value in updated_post.dict().items():
    setattr(db_post, key, value)
  session.commit()
  return db_post
```

---
zoom: 0.8
transition: fade
level: 3
---

## PATCH

PATCH actualiza parcialmente un recurso existente, sin necesidad de reemplazarlo completamente.

Por ejemplo, `PATCH /posts/14` puede actualizar solo el título del post.
```py
from typing import Optional
from pydantic import BaseModel

class PostPatch(BaseModel):
  title: Optional[str] = None
  content: Optional[str] = None

@app.patch(
  '/posts/{post_id}',
  response_model=PostOut
)
async def patch_post(
  post_id: int,
  post_data: PostPatch,
  session: Depends(get_db)
):
  db_post = session.query(Post).filter(Post.id == post_id).first()
  if db_post is None:
    raise HTTPException(status_code=404, detail="Post no encontrado")
  for key, value in post_data.dict(exclude_unset=True).items():
    setattr(db_post, key, value)
  session.commit()
  return db_post

```

---
zoom: 0.8
transition: fade
level: 3
---

## DELETE

Una petición DELETE elimina un recurso del servidor.

Por ejemplo, `DELETE /posts/14` elimina el post con ID 14.

```py
@app.delete(
  '/posts/{post_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_post(
  post_id: int,
  session: Depends(get_db)
):
  db_post = session.query(Post).filter(Post.id == post_id).first()
  if db_post is None:
    raise HTTPException(status_code=404, detail="Post no encontrado")
  session.delete(db_post)
  session.commit()
  return None
```


---
zoom: 0.8
layout: quote
transition: zoom
---

## Depends en FastAPI

`Depends` es un **sistema de inyección de dependencias** que permite **reutilizar lógica común** en distintos endpoints, como conexiones a base de datos, autenticación o validaciones.

---

### Concepto básico

<v-clicks>

- Una **dependencia** es una función que devuelve un valor que otro endpoint necesita.  
- FastAPI la ejecuta automáticamente antes de llamar al endpoint.  
- El valor devuelto se inyecta como parámetro.  

</v-clicks>

<v-click>

```py
from fastapi import Depends

def get_query_token():
  return "token123"

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(get_query_token)]):
  return {"token": token}
```

Es lo que hemos estado usando para obtener la sesión a la base de datos. `Depends` permite cualquier tipo de función:

</v-click>

<v-clicks>

- Funciones normales (`def`)
- Generadores (con `yield` en lugar de `return`)
- Funciones asíncronas (`async def`)

</v-clicks>


---
layout: default
level: 2
zoom: 0.9
transition: fade
---

# Autenticación

En muchas APIs suele haber determinadas rutas protegidas, de forma que no cualquier usuario puede llamar a esas funciones. Vamos a aplicar una especificación llamada **JWT**. La libreria en Python de esta especificación se llama **PyJWT**.

````md magic-move {lines: true}

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt  # PyJWT

# indica que el endpoint /login es el que genera tokens a partir de un formulario Usuario - Contraseña
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "clave_secreta" # mejor guardarlo en .env, para el taller lo omitimos
ALGORITHM = "HS256"
```
```py
def verify_token(token: Annotated[str, Depends(oauth2_scheme)]) -> str:
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    if email is None:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido"
      )
    return email
  except jwt.ExpiredSignatureError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Token expirado"
    )
  except jwt.InvalidTokenError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Token inválido"
    )
```

```py
from datetime import datetime, timedelta

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=120)
  to_encode.update({"exp": expire})
  token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return token
```

```py
def get_current_user(
  email: Annotated[str, Depends(verify_token)],
  session: Annotated[Session, Depends(get_db)]
):
  db_user = session.query(User).filter(User.email == email).first()
  if db_user is None:
    raise HTTPException(status_code=401, detail="No tienes acceso para realizar esta petición")
  return db_user

CurrentUser = Annotated[User, Depends(get_current_user)]

@app.get(
  '/users/me',
  response_model=UserOut
)
async def get_me(current_user: CurrentUser):
  return current_user
```
````

<v-click>

Como podemos ver, la introducción de dependencias mejora mucho la tarea de validar tokens y autenticación del usuario.

</v-click>



---
transition: slide-left
level: 2
---

# Routers

Ya tenemos todos los ingredientes para montar nuestra API. Solo hay un pequeño detalle todavía por cubrir, si nuestra API es muy grande, no es recomendable almacenar los endpoints en el mismo fichero. Lo ideal es **separar lógicamente** los endpoints según ciertos criterios o categorías.

::code-group

```py [users.py]
from fastapi.routing import APIRouter

router = APIRouter(
  prefix='/users', tags=['users']
)

@router.get('/{user_id}')
async def get_user(user_id: int, session: Annotated[Session, Depends(get_db)]):
  return session.query(User).filter(User.id == user_id).first()
```

```py [posts.py]
from fastapi.routing import APIRouter

router = APIRouter(
  prefix='/posts', tags=['posts']
)

@router.get('/{post_id}')
async def get_post(post_id: int, session: Annotated[Session, Depends(get_db)]):
  return session.query(Post).filter(Post.id == post_id).first()
```

```py [comments.py]
from fastapi.routing import APIRouter

router = APIRouter(
  prefix='/comments', tags=['comments']
)

@router.get('/{comment_id}')
async def get_comment(comment_id: int, session: Annotated[Session, Depends(get_db)]):
  return session.query(Comment).filter(Comment.id == comment_id).first()
```

```py [main.py]
from routers import users, posts, comments

app = FastAPI(...)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
```

::


---

## Estructura de ramas

<v-click>

- **1 única rama principal** (main/master) → siempre estable
- **No pushear NUNCA directamente a main**
- **Pull Requests** para todos los cambios
- **Separar dev y release** si es necesario

</v-click>

<v-click>

## Workflow recomendado

```bash
git pull origin main          # Actualizar main
git checkout -b feature/nueva-funcionalidad
# ... hacer cambios ...
git add .
git commit -m "feat: add nueva funcionalidad"
git push origin feature/nueva-funcionalidad
# Abrir Pull Request en GitHub/GitLab
```

</v-click>

---

## Conventional Commits

[conventionalcommits.org](https://www.conventionalcommits.org/en/v1.0.0/)

<v-click>

```bash
feat: nueva funcionalidad
fix: corregir bug
docs: actualizar documentación
style: cambios de formato
refactor: refactorizar código
test: añadir tests
chore: tareas de mantenimiento
```

</v-click>

<v-click>

## Semantic Versioning

[semver.org](https://semver.org/)

</v-click>

<v-click>

`MAJOR.MINOR.PATCH` → `1.4.2`

- **MAJOR**: Cambios incompatibles
- **MINOR**: Nueva funcionalidad compatible
- **PATCH**: Bug fixes compatibles

</v-click>

---
zoom: 0.85
---

# Merge conflicts

Los conflictos ocurren cuando Git no puede fusionar automáticamente los cambios de diferentes ramas.

<v-click>

## ¿Cuándo suceden?

- Dos personas modifican la misma línea de código
- Una persona elimina un archivo que otra ha modificado
- Cambios incompatibles en la estructura del proyecto

</v-click>

<v-click>

## Resolución

```bash
git merge feature-branch
# CONFLICT (content): Merge conflict in file.txt
# Automatic merge failed; fix conflicts and then commit the result.
```

</v-click>

<v-click>

1. Abrir el archivo con conflictos
2. Buscar las marcas `<<<<<<<`, `=======`, `>>>>>>>`
3. Decidir qué cambios mantener
4. Eliminar las marcas de conflicto
5. `git add` y `git commit`

</v-click>

---
layout: cover
level: 2
---

# Resolución forzosa ⚠️☠️

<v-click>

```bash
git reset --hard <branch>
```

</v-click>

---
layout: two-cols
---

# .gitignore

Un fichero especial que le dice a Git qué archivos o directorios ignorar.

<v-click>

**¿Por qué es importante?**

- Evitar subir archivos temporales
- No versionar credenciales
- Ignorar dependencias que se pueden regenerar
- Mantener el repo limpio

</v-click>

<v-click>

**Sintaxis básica**

```md [.gitignore]
# Comentarios
*.log          # Todos los .log
node_modules/  # Directorio completo
!important.log # Excepción
temp*          # Archivos que empiecen por temp
```

</v-click>

::right::

<v-click>

## Ejemplos comunes

```md [gitignore]
# Dependencias
node_modules/
venv/
.env

# Archivos del sistema
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp

# Builds
dist/
build/
*.o
*.exe

# Logs
*.log
logs/

# Credenciales
.env
config/secrets.json
```

</v-click>

---
transition: slide-up
zoom: 0.85
---

# Git Hooks

Scripts que se ejecutan automáticamente en ciertos eventos de Git.

<v-click>

## Tipos principales

<div class="grid grid-cols-2 gap-4">
<div>

### Client-side
- `pre-commit`: Antes de cada commit
- `prepare-commit-msg`: Preparar mensaje
- `commit-msg`: Validar mensaje
- `post-commit`: Después del commit

</div>
<div>

### Server-side
- `pre-receive`: Antes de recibir push
- `update`: Por cada rama actualizada
- `post-receive`: Después del push

</div>
</div>

</v-click>

<v-click>

## Ejemplo: pre-commit

```bash
#!/bin/sh
# .git/hooks/pre-commit

# Ejecutar tests antes de commitear
npm test
if [ $? -ne 0 ]; then
  echo "Tests fallaron. Commit cancelado."
  exit 1
fi

# Verificar formato de código
npm run lint
```

</v-click>

---
zoom: 0.7
---

# GitOps

<v-click>

## Filosofía de desarrollo

> "Git como única fuente de verdad para la infraestructura y aplicaciones"

[Ejemplo: k8s Ingress](https://kubernetes.io/es/docs/concepts/services-networking/ingress/#el-recurso-ingress)

</v-click>

<v-click>

## Principios clave

</v-click>

<v-clicks>

- **Declarativo**: Todo se describe en archivos de configuración
- **Versionado**: Toda la configuración está en Git
- **Inmutable**: Los cambios se hacen via pull requests
- **Reconciliación continua**: Herramientas automatizan el despliegue

</v-clicks>

<v-click>

## Herramientas populares

- **ArgoCD** / **Flux** (Kubernetes)
- **Terraform** + **Atlantis**
- **GitHub Actions** / **GitLab CI**

</v-click>

<v-click>

## Beneficios

✅ Trazabilidad completa  
✅ Rollbacks fáciles  
✅ Colaboración via PR  
✅ Auditoría automática

</v-click>

---
layout: cover
---

# Lazygit

Una interfaz de terminal para Git más visual e intuitiva.

---
layout: two-cols
image: https://github.com/jesseduffield/lazygit/raw/master/docs/resources/demo.gif
backgroundSize: contain
---

**Instalación**

<v-click>

```bash
brew install lazygit  # macOS

sudo apt install lazygit  # Ubuntu/Debian

scoop install lazygit  # Windows
```

</v-click>

<v-click>

**Características principales**

- **Interfaz visual** para el estado del repo
- **Navegación con teclado** intuitiva
- **Staging interactivo** de cambios
- **Resolución visual** de merge conflicts
- **Historial gráfico** de commits
- **Gestión de ramas** simplificada

</v-click>

::right::

<v-click>

**Uso básico**

- Navegación: ↑↓←→, Tab, Enter, Esc
- Staging: Espacio
- Commit: c
- Push: P


```bash
lazygit
```

</v-click>

---
layout: center
class: text-center
---

# ¡Gracias por asistir!

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    ¿Preguntas? 🤔
  </span>
</div>

<div class="pt-12">

## Recursos útiles

[📖 Pro Git Book](https://git-scm.com/book) • [🎮 Learn Git Branching](https://learngitbranching.js.org/) • [📚 Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/jorgegomzar" target="_blank" alt="GitHub" title="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

