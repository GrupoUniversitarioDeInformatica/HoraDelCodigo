from fastapi import FastAPI
from database import Base, engine
from routers import users, posts, comments

# Crear tablas si no existen (seguro con el init.sql; para el taller viene bien)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fullstack Workshop API", root_path='/api')

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
