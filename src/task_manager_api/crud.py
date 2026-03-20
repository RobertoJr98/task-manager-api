from sqlalchemy.orm import Session

from . import models, schemas
from ...app.core.security import hash_password, verify_password


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, email: str, password: str) -> models.User:
    user = models.User(
        email=email,
        hashed_password=hash_password(password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str) -> models.User | None:
    user = get_user_by_email(db, email)

    if not user:
        return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    return user

def create_task(db: Session,user_id: int, task: schemas.TaskCreate):

    db_task = models.Task(
        title=task.title,
        description=task.description,
        owner_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_tasks_by_user(db: Session, user_id: int):

    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

def get_task(db: Session, task_id: int):

    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db:Session, task: models.Task, payload: schemas.TaskUpdate):

    if payload.title is not None:
        task.title = payload.title

    if payload.description is not None:
        task.description = payload.description

    if payload.completed is not None:
        task.completed = payload.completed

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task: models.Task):

    db.delete(task)
    db.commit()