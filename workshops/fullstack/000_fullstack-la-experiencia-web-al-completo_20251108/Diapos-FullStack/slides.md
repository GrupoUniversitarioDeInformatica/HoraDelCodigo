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
  session: Annotated[Session, Depends(get_db)]
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
  session: Annotated[Session, Depends(get_db)]
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
  session: Annotated[Session, Depends(get_db)]
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
  session: Annotated[Session, Depends(get_db)]
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
  session: Annotated[Session, Depends(get_db)]
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
  session: Annotated[Session, Depends(get_db)]
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

```python {*|6,8,9|*}
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt  # PyJWT

# indica que el endpoint /login es el que genera tokens a partir de un formulario Usuario - Contraseña
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "clave_secreta" # mejor guardarlo en .env, para el taller lo omitimos
ALGORITHM = "HS256"
```
```py {*|1,3|*}
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

```py {*|7|*}
from datetime import datetime, timedelta

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=120)
  to_encode.update({"exp": expire})
  token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return token
```

```py {*|2,3|10|12-17|*}
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
transition: fade
level: 2
zoom: 0.9
---

## Política CORS

CORS = Cross Origin Resource Sharing

<v-clicks>

- Aparece cuando se hacen peticiones desde otros servidores.
- La cabecera **Origin** indica la URL desde donde se hace la petición.
- Nosotros, en el BackEnd, podemos decir desde qué URLs queremos recibir peticiones.
- Atención: Esta política solo surge efecto si se hace una petición desde un servidor externo. Si nosotros nos comunicamos directamente con nuestra API, la política CORS no tiene efecto alguno.

</v-clicks>

<v-click>

````md magic-move {lines: true}
```py
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(...)

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:5173",
    "http://localhost:4173",
    "https://localhost:8443",
    "https://localhost"
  ],
  allow_methods=['*'],
  allow_headers=['*'],
  allow_credentials=True,
)
```
````

</v-click>

---
layout: cover
level: 1
---

# Desarrollo FrontEnd

---
layout: two-cols
level: 2
transition: slide-left
---

## Reactividad

- La reactividad es la capacidad de un sistema de cambiar de forma dinámica sin necesidad de actualizar forzosamente una página.

<br>

<img src="https://imgs.search.brave.com/nrRCx3Hk71NnpsNL34Mv0Ci1to4k2dh5I4fnC1S2FCs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9hbmd1/bGFyLWxvZ28tZWRp/dG9yaWFsLWlsbHVz/dHJhdGl2ZS13aGl0/ZS1iYWNrZ3JvdW5k/LWFuZ3VsYXItbG9n/by1lZGl0b3JpYWwt/aWxsdXN0cmF0aXZl/LXdoaXRlLWJhY2tn/cm91bmQtZXBzLWRv/d25sb2FkLTIwODMy/OTExOS5qcGc" class="w-50 ml-20">

<br>

- Con Vue podremos crear referencias a datos que se actualizan de forma dinámica cuando cambian esos datos.

::right::

<img src="https://imgs.search.brave.com/SP8815zx7oKRZ0A6Ak3zvOZDSzs_YWn6JJfGAqALOuQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy82/MmE3NGRkMTIyMzM0/M2ZiYzIyMDdkMDAu/cG5n" class="w-50 ml-30" />

<br>

- Crear páginas reactivas sin el uso de *frameworks* es una tarea bastante complicada, por lo que usaremos una librería de **Node** llamada **Vue.js**.

<br>

<img src="https://imgs.search.brave.com/l1RNtSSSLn-gCpmJxG8RnBe_AeKK1sBlnApBK3stHKs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/YnJhbmRmZXRjaC5p/by9pZFQtN2FMQ0Fq/L3RoZW1lL2Rhcmsv/bG9nby5zdmc_Yz0x/YnhpZDY0TXVwN2Fj/emV3U0FZTVgmdD0x/NzQ4Mjg2NzU1NTY3" class="w-40 ml-35">

<v-click>

</v-click>

---
transition: fade
zoom: 0.7
level: 2
---

## HTML + CSS + JavaScript

<div class="grid grid-cols-3 mt-3">
  <div> 
    <h3 class="text-center underline text-gray-700"> HTML </h3>
    <h5 class="text-center"> HyperText Markup Language </h5>
    
  </div>
  <div>
    <h3 class="text-center underline text-gray-700"> CSS </h3>
    <h5 class="text-center"> Cascade Style Sheets </h5>
  </div>
  <div> 
    <h3 class="text-center underline text-gray-700"> JavaScript </h3>
    <h5 class="text-center"> No, esto no es Java, es peor </h5>
  </div>
</div>
```html
<html>
  <head>
    <!-- CSS -->
    <style>
      .boton {
        background-color: green;
        color: white;
      }
      .otro-boton {
        background-color: black;
        color: white;
      }
    </style>
  </head>
  <body>
    <div>
      <button class="boton"> Botón </button>
    </div>
    <!-- JavaScript -->
    <script>
      let clase = 0;
      const boton = document.querySelector('.boton');
      function changeClass() {
        boton.classList.remove( clase ? 'boton' : 'otro-boton');
        boton.classList.add( clase ? 'otro-boton': 'boton' );
        clase = (clase + 1) % 2;
      }
      boton.addEventListener('click', changeClass);
    </script>
  </body>
</html>
```

---
transition: fade
level: 2
---

## TailwindCSS
**TailwindCSS** es una librería de Node, que trae incluído un surtido extremadamente variado de estilos. En resumen, se podrán diseñar y construir páginas web. No tendremos que diseñar ni un solo estilo, Tailwind nos da una serie de clases pre-hechas para usar en el momento.

Varios ejemplos de clases de tailwind:
<v-clicks>

- <div class="text-red-500"> text-red-500 </div>
- <div class="text-4xl"> text-4xl </div>
- <div class="border rounded-lg text-center border-green-300"> border rounded-lg text-center border-green-300</div>
- <div class="hover:border rounded-lg text-center hover:text-gray-400 border-blue-400 transition-all duration-150"> hover:border rounded-lg text-center hover:text-gray-400 border-blue-400 transition-all duration-150 </div>
- <div class="bg-gradient-to-tr from-fuchsia-500 to-cyan-500 bg-clip-text text-transparent"> bg-gradient-to-tr from-cyan-300 to-blue-700 bg-clip-text text-transparent </div>

</v-clicks>

<v-click>

Enlace a un generador de gradientes para Tailwind: [Tailwind Generator](https://www.creative-tim.com/twcomponents/gradient-generator)

</v-click>

---
level: 2
transition: slide-left
---

# Vue.js

### Reactividad en Vue

Para implementar la reactividad en Vue, habitualmente se usa una función llamada `ref`. Esto crea una referencia a un wrapper de datos (un envoltorio sobre un tipo concreto), que, al actualizar el dato internamente, lanza una actualización a la vista para que la interfaz cambie visualmente.

Ejemplo:

```vue
<template>
  <button @click="contador++"> {{ contador }} </button>
  <!-- Si cambia internamente la variable contador, el texto {{ contador }} se actualiza dinámicamente -->
</template>
<script>
import { ref } from 'vue';
const contador = ref(0);
</script>
```

---
level: 2
transition: fade
---

# Distintos métodos reactivos en Vue

<v-click>

- `ref`: Referencia dinámica a un objeto.

</v-click>
<v-click>

- `computed`: Cada vez que se usa esta variable, se calcula el contenido mediante una función. Ejemplo:
```js
const computado = computed(() => x + 5); // suponiendo que x es una variable externa.
```
</v-click>

<v-click>

- `reactive`: Se aplica a un objeto. Aplica internamente `ref` a los atributos del objeto.

</v-click>

<v-click>
<br>

### Funciones adicionales reactivas
- `watch`: Observa cambios en una variable y ejecuta una rutina personalizada al cambiar. Ejemplo:
```js
import { ref, watch } from 'vue';

const x = ref(0);
watch(
  x,
  () => {
    console.log(`x (${x.value}) ha cambiado de valor`)
  }
)
```
</v-click>

---
level: 2
transition: fade
zoom: 1.1
---

# Vistas y componentes

En Vue existen dos principales conceptos agrupados alrededor de la misma idea: **Componentes**.

Un componente es una abstracción reutilizable de código HTML + Vue. 
Es decir, que los componentes pueden estar formados de código HTML y Vue. 
Cualquier fichero `.vue` puede ser tratado como un componente individual. Ejemplo:

::code-group
```vue [ContadorNumero.vue]
<script setup>
import { ref } from 'vue';
const contador = ref(0);
</script>
<template>
  <button @click="contador++"> {{ contador }} </button>
</template>
```
```vue [App.vue]
<script setup>
import ContadorNumero from './ContadorNumero.vue';
</script>
<template>
  <h1> Ejemplo de contador </h1>
  <ContadorNumero /> <!-- Inserta el componente en la vista -->
</template>
```
::

<v-click>
<br>

Habitualmente se separan en dos grupos: **Componentes** y **Vistas**.

</v-click>

---
level: 2
transition: fade
zoom: 1
---

# Componentes

Generalmente, los componentes reciben parámetros. Podríamos compararlos con las clases en programación orientada a objetos, como si fuesen el constructor de la clase. A este constructor se le llaman `props` (propiedades).

<v-click>

```vue {*}{maxHeight:'350px'}
<!-- PresentationCard.vue -->
<script setup>
const props = defineProps({
  name: { type: String, required: true },
  description: { type: String, required: false }.
  hobbies: { type: String[], required: false, default: () => [] }
});
</script>
<template>
  <div class="max-w-md mx-auto bg-white rounded-2xl shadow-md p-6 border border-gray-100">
    <h2 class="text-2xl font-bold text-gray-800 mb-2">{{ name }}</h2>
    <p v-if="description" class="text-gray-600 mb-4">
      {{ description }}
    </p>
    <div v-if="hobbies.length" class="mt-4">
      <h3 class="text-lg font-semibold text-gray-700 mb-2">Hobbies</h3>
      <ul class="flex flex-wrap gap-2">
        <li 
          v-for="(hobby, index) in hobbies" 
          :key="index" 
          class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm"
        >
          {{ hobby }}
        </li>
      </ul>
    </div>
    <div v-else class="text-gray-400 italic mt-4">
      No hobbies listed.
    </div>
  </div>
</template>
```

</v-click>

---
level: 2
transition: fade
---

# Vistas

En Vue, una vista es un componente con un comportamiento ligeramente distinto.

Se programan de la misma manera que los componentes. Las vistas también pueden recibir `props`.

La diferencia es que no se usan colocando la vista en el código como los componentes. Ejemplo:
````md magic-move {lines: true}
::code-group
```vue 
<!-- App.vue, uso de componentes -->
<script setup>
import MiComponente from './MiComponente.vue';
</script>
<template>
  <MiComponente />
</template>
```
```vue
<!-- App.vue, uso de vistas -->
<script setup>
</script>
<template>
  <router-view /> <!-- Componente especial de Vue -->
</template> 
```
````

<v-click>

Vue analiza la **URL** del navegador y muestra la vista correspondiente a esa URL.

Para que Vue reconozca las rutas hay que usar una libreria complementaria llamada `vue-router`.

</v-click>


---
level: 2
transition: fade
zoom: 0.92
---

# Vue Router

Para definir el router, hay que seguir un esquema muy sencillo:

```js
// ./router/index.js
import HomePage from '@/views/HomePage.vue'
const routes = [{
    path: '/',
    name: 'home',
    component: HomePage,
    meta: { requiresAuth: false, guestOnly: false },
    children: []
  },
  {
    path: '/users',
    name: 'users',
    component: () => import('@/views/UsersPage.vue'), // forma alternativa
    meta: { requiresAuth: true, guestOnly: false },
    children: [
      {
        path: ':userId', // parámetro, para entrar en /users/15, por ejemplo
        name: 'singleUser',
        component: () => import('@/views/SingleUserPage.vue'),
        meta: { requiresAuth: false, guestOnly: false },
        children: []
      }
    ]
  }
]
```

---
level: 2
transition: fade
---

# Router Link

Para enrutar las distintas vistas, se puede usar otro componente especial de Vue llamado `<RouterLink>` Ejemplo:

```vue
<script setup>

</script>
<template>
  <RouterLink :to="{name: 'users'}" > <!-- Enruta en base a la propiedad `name` del router -->
    Usuarios
  </RouterLink>

  <router-view /> <!-- Al darle al enlace de arriba, este componente se sustituirá por la vista `UsersPage`-->
</template>
```

---
level: 2
transition: fade
---

# Emits: Eventos customizados para componentes
Los emits sirven para que un componente envíe, o exponga eventos personalizados al componente que lo usa. 

El componente en cuestión define un `emit('nombre', parametros)` y el padre (el que usa al otro componente) llama al evento mediante `@nombre=f(parametros)`.

::code-group
```vue [Hijo.vue]
<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['pepe']);

function notify() {
  emit('pepe', 'un mensaje');
}
</script>
<template>
  <button @click="notify"> Emitir Evento </button>
</template>
```

```vue [Padre.vue]
<script setup>
import Hijo from './Hijo.vue';
</script>
<template>
  <Hijo @pepe="(msg) => console.log(msg)" />
</template>
```
::

<v-click>

Al hacer click al botón en el componente del Hijo, el Padre imprimirá por pantalla el mensaje que le pasa el hijo. Es una forma de obtener datos que se encuentran en componentes inferiores y recuperarlos en los padres.

</v-click>

---
level: 2
transition: fade
---

# Atributos personalizados de Vue

Vue añade nuevos atributos a cada etiqueta de HTML. Vamos a dar un repaso a todos ellos. **Nota**: muchas de las siguientes directivas solo se pueden usar con variables reactivas (`ref`, `computed`, `reactive`).

<v-clicks>

- `v-if`: La etiqueta se renderiza bajo una condición. Ejemplo: `<p v-if="error"> {{ error }} </p>`
- `v-else-if`: De forma similar, pero necesita previamente un `v-if`.
- `v-else`: La última alternativa para condicionales, se renderiza si ninguna de las anteriores condiciones se cumple.

</v-clicks>
<v-click>

- `v-for`: Itera sobre una lista, pudiendo usar sus contenidos dentro:

```vue
<!-- Crea una lista no ordenada con todos los elementos del array `items` -->
<ul>
  <li v-for="(item, idx) in items" :key="idx"> {{ item }} </li>
</ul>
```
</v-click>

---
level: 2
transition: fade
---

# Modificadores de atributos

Vue permite alterar el comportamiento de los atributos HTML mediante las siguientes extensiones:

<v-click>

- `v-model="variable_reactiva"`: Habitualmente usada en las etiquetas de tipo `<input>` o `<button>`, en general aquellas que reciben entradas de usuarios. Al cambiar el valor del input también se cambia el valor de la variable de forma automática. Es como asignar la variable a ese input en concreto.
````md magic-move {lines: true}
```vue 
<script setup>
import { ref, watch } from 'vue';
const edad = ref(18);

watch(
  edad,
  () => console.log(`Edad ha cambiado: ${edad.value}`),
);
</script>
<template>
  <label class="flex flex-row">
    <p> Introduce tu edad </p>
    <input type="number" v-model="edad">
  </label>
</template>
```
````

</v-click>

---
transition: fade
---

- `:atributo`: Permite introducir variables reactivas dentro del valor del atributo HTML. Por ejemplo, si implementamos un modo claro y un modo oscuro:

<v-click>

````md magic-move {lines: true}
```vue
<script setup>
import { ref } from 'vue';
const modoOscuro = ref(false);
</script>
<template>
  <button @click="modoOscuro = !modoOscuro"> Cambiar Aspecto </button>
  <div class="container w-30 h-30 rounded-lg" 
    :class="modoOscuro ? 'bg-gray-950 text-white' : 'bg-gray-50 text-black'"
  > Contenido ... </div>
</template>
```
````
</v-click>

<v-click>

- `v-html`:  **ATENCIÓN**: Permite renderizar código HTML con el contenido de una variable reactiva. Muy versátil, pero al mismo tiempo **muy** peligroso. ¿Qué pasaría si alguien introduce una etiqueta `<script>` dentro del HTML y accede a nuestros recursos? Es una forma de ciberataque! Si se usa esta etiqueta, que sea de forma controlada y nunca permitir que los usuarios puedan acceder a este tipo de atributos de Vue.

</v-click>

---
transition: fade
---

- `@evento`: Asigna una función o línea de código a un evento en concreto. En las anteriores diapositivas ya se han mostrado ejemplos sobre cómo funciona este modificador.

<v-click>

- `{{ variable_dinamica }}`: Permite introducir de forma dinámica referencias en el código. Se puede ver en el ejemplo del `v-for`.

</v-click>

---
transition: fade
level: 2
---

# Funciones especiales de Vue

Vue tiene ciertas funciones especiales que permiten ejecutar código antes de la creación de un componente, y tras la destrucción de un componente: `onMounted` y `onUnmounted`.

- `onMounted`: Ejecuta una función en el momento en el que el componente se cargue en la página web. Por ejemplo, si esa vista en concreto depende del Backend por un dato, que lance la petición en el momento en el que se cargue el componente. Ejemplo:

<v-click>
```vue {*|14-16|19|*}{maxHeight:'280px'}
<script setup>
import { ref, onMounted } from 'vue';
import { useXController } from '@/composables';
import XCard from '@/components'

const props = defineProps({
  id: { type: Number, required: true }
});

const { getX } = useEventsController();

const x = ref(undefined);

onMounted(async () => {
  x.value = await getX(props.id); // cargamos el dato
})
</script>
<template>
  <XCard :x="x" />
</template>
```


</v-click>

---
transition: fade
---

- `onUnmounted`: Lo mismo, pero en el momento de destrucción del componente. Por ejemplo, guardar el estado tras cerrar una ventana:

```vue {*}
<script setup>
import { onUnmounted } from 'vue';
import { useLocalStore } from '@/stores'
// esta función no existe, es solo un ejemplo
const { saveChanges } = useLocalStore();
onUnmounted(() => {
  saveChanges(); // al destruir el componente, guarda los cambios de forma local
})
</script>
<template>
  <div> ... </div>
</template>
```

---
transition: fade
level: 2
---

# Generadores de clientes a partir de OpenAPI

Para evitar tener que programar manualmente las peticiones HTTP, podemos generar un cliente que coja la documentación OpenAPI descrita en el Backend.

<v-click>

```sh
# instala el generador de clientes
npm install @openapitools/openapi-generator-cli -g # -g de forma global

# usa una versión específica de la librería
openapi-generator-cli version-manager set 7.15.0

# genera el cliente a partir de la documentación creada en el backend
openapi-generator-cli generate -i https://localhost:8443/openapi.json -g javascript -o /src/api

```

</v-click>

<v-click>

Podeis ver todos los generadores distintos en esta página: [Generadores OpenAPI](https://openapi-generator.tech/docs/generators)

También existen generadores para BackEnd, aunque esos ya no los necesitamos ;)

</v-click>

---
level: 1
transition: fade
layout: end
---


# Fin

## Espero que os haya gustado!

### [Nuestro GitHub](https://github.com/GrupoUniversitarioDeInformatica)

### [Enlace al Repo](https://github.com/GrupoUniversitarioDeInformatica/HoraDelCodigo)
