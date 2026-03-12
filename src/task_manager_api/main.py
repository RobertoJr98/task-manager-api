from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas, crud
from .security import create_access_token
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
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, payload.email, payload.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )
    
    token = create_access_token({"sub": user.email})
    
    return {"access_token": token, "token_type": "bearer"}