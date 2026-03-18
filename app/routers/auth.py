from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.schemas import user as user_schema
from app.models import user as user_model
from app.crud import user as user_crud
from app.core.security import create_access_token, verify_password, get_current_user, hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# Endpoint para registro de novos usuários
@router.post("/register", response_model=user_schema.UserResponse)
def register_user(
    payload: user_schema.UserCreate,
    db: Session = Depends(get_db)
):
    user = user_crud.get_user_by_email(db, payload.email)

    if user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    new_user = user_crud.create_user(db, payload.email, payload.password)

    return new_user


# Endpoint para login e obtenção do token de acesso(JWT)
@router.post("/login", response_model=user_schema.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )
    
    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Endpoint para obter informações do usuário autenticado
@router.get("/me", response_model=user_schema.UserResponse)
def read_me(current_user: user_model.User = Depends(get_current_user)):
    return current_user
