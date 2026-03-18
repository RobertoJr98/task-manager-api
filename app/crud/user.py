from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from app.core.security import hash_password, verify_password


def get_user_by_email(db: Session, email: str) -> user_model.User | None:
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def create_user(db: Session, email: str, raw_password: str) -> user_model.User:
    user = user_model.User(
        email=email,
        hashed_password=hash_password(raw_password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str) -> user_model.User | None:
    user = get_user_by_email(db, email)

    if not user or not verify_password(password, user.hashed_password):
        return None
    
    return user
