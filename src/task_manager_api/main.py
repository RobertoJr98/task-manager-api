from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from .database import Base, engine, get_db
from . import models, schemas, crud
from .security import create_access_token, get_current_user
from .schemas import LoginRequest, Token

app = FastAPI(title="Task Manager API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Task Manager API is running"}

@app.post("/users", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-mail já cadastrado",
        )
    
    user = crud.create_user(db, email=payload.email, password=payload.password)
    return user

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )
    
    token = create_access_token({"sub": user.email})
    
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=schemas.UserResponse)
def read_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    payload: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    task = crud.create_task(db, current_user.id, payload)

    return task

@app.get("/tasks", response_model=List[schemas.TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: models.User =Depends(get_current_user)
):
    tasks = crud. get_tasks_by_user(db, current_user.id)

    return tasks

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    payload: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    task = crud.get_task(db, task_id)

    if not task or task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    
    updated = crud.update_task(db, task, payload)

    return updated

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    
    task = crud.get_task(db, task_id)

    if not task or task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    
    crud.delete_task(db, task)

    return {"message": "Task deletada"}