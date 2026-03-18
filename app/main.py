from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks, auth

#Inicializa a aplicação FastAPI
app = FastAPI(title="Task Manager API")

#Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)

#Registra os routers
app.include_router(auth.router)
app.include_router(tasks.router)

#Endpoint raiz para verificar se a API está funcionando
@app.get("/")
def root():
    return {"message": "Task Manager API is running"}
