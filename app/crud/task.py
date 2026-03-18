from sqlalchemy.orm import Session
from app.models.task import Task as models_task
from app.schemas import task as schemas_task

def create_task(db: Session, user_id: int, payload: schemas_task.TaskCreate) -> models_task:

    db_task = models_task(
        title=payload.title,
        description=payload.description,
        owner_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_tasks_by_user(db: Session, user_id: int) -> list[models_task]:

    return db.query(models_task).filter(models_task.owner_id == user_id).all()

def get_task(db: Session, task_id: int) -> models_task | None:

    return db.query(models_task).filter(models_task.id == task_id).first()

def update_task(db:Session, task: models_task, payload: schemas_task.TaskUpdate) -> models_task:

    if payload.title is not None:
        task.title = payload.title

    if payload.description is not None:
        task.description = payload.description

    if payload.completed is not None:
        task.completed = payload.completed

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task: models_task) -> None:

    db.delete(task)
    db.commit()