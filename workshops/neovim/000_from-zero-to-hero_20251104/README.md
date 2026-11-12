# NEOVIM - From zero to hero

- Autor: Jorge Gómez Zarzosa
- Fecha de adición: 2025-11-04 19:17:54

---

## Descripción

Este taller va de enseñar a utilizar y configurar el editor de texto nvim (Neovim) desde 0
hasta acabar con un editor de código funcional.

Se explicará:

- Como moverse dentro de vim + vim motions
  - Una versión express de vimtutor
  - Como consultar documentación desde neovim
- Terminología básica de vim:
  - Modos
  - Buffers
  - Windows
  - Tabs
  - Registros
  - Marcadores
  - Macros
  - Keybindings
- Lua
- Terminología avanzada:
  - vim.o, vim.b, vim.g,...
  - vim.api
    - nvim_create_augroup
    - nvim_create_autocmd
    - nvim_create_user_command
    - nvim_buf_create_user_command
  - vim.lsp
- Plugins
  - Plugin manager
    - [Roadmap neovim](https://dotfyle.com/neovim/plugins/trending)
    - [Lazyvim](https://github.com/LazyVim/LazyVim)
  - [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig/)
  - conform
  - Snacks
- VCS --> GitHub o similar
  - CUIDADO CON LOS SECRETS

## Requisitos

Se recomienda a los participantes que:

- Vengan con un ordenador portátil propio (SO preferentemente GNU: linux / macos. Aunque no es obligatorio)
- Sepan manejarse un mínimo en el terminal y Git

Esto son recomendaciones, neovim es multiplataforma y cualquier duda que surja durante el taller será aclarada
allí mismo.

## Otros detalles

Para el que quiera dar este taller, recomiendo que:

1. Haya pasado por la experiencia de configurar neovim desde 0 al menos una vez (NvChad o frameworks similares no cuentan, salvo que realmente le hayáis metido horas, vaya).
2. Tengáis la configuración guardada en un servicio de VCS como GitHub.
3. Probéis a llegar desde un neovim limpio (sugiero usar un contenedor de Docker para esto)


### Enlaces de interés

- [Neovim vision](https://neovim.io/charter/)
- [Neovim roadmap](https://neovim.io/roadmap/)
- [Una observación realista sobre editores de texto](https://www.reddit.com/r/neovim/comments/158voa9/comment/jtcwvuj/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
- [Lazyvim](https://www.lazyvim.org/)
- [Mi neovim-config](https://github.com/jorgegomzar/nvim-config)

### FAQ

#### ¿Qué diferencias tiene neovim respecto a vim?

1. Tiene un núcleo moderno y asíncrono
2. Usa Lua de forma nativa, permitiendo plugins más rápidos y potentes
3. Trae LSP y Tree-sitter integrados
4. Tiene un ecosistema de plugins moderno y activo
5. Es más fácil de extender y más fluido para trabajar

Vim sigue siendo excelente, pero es más conservador y limitado internamente.

#### ¿Qué es LSP (Language Server Protocol)?

Un estándar para que el editor hable con un *servidor de lenguaje* (Python, Rust, TS…).

Proporciona autocompletado inteligente, ir a definición, renombrar símbolos, diagnósticos, etc., igual que VSCode.

#### ¿Qué es Tree-sitter?

Un parser moderno que entiende la sintaxis real del código (no solo regex), mediante AST.

Permite coloreado más preciso, mejor indentación, folding inteligente y análisis estructural del archivo.

#### ¿Qué es LazyVim?

Una configuración prearmada de Neovim basada en el plugin manager **lazy.nvim**.

Incluye un ecosistema de plugins ya listos (LSP, treesitter, telescope, UI moderna…) para tener un editor completo sin configurarlo tú desde cero.

#### ¿Qué es mason.nvim?

**mason.nvim** es un gestor de paquetes para Neovim que instala y administra herramientas externas como **LSP servers**, **linters**, **formatters** y **DAP**.

Simplifica el proceso de instalarlos (sin usar npm, pip, brew, etc.) y los integra fácilmente con plugins como `lspconfig` o `null-ls`.

