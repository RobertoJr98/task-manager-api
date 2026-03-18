from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import task as crud_task
from app.schemas import task as task_schemas
from app.models import user as user_model
from app.core.security import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags= ["Tasks"]
)

@router.post("/", response_model=task_schemas.TaskResponse)
def create_task(
    payload: task_schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    task = crud_task.create_task(db, current_user.id, payload)

    return task

@router.get("/", response_model=List[task_schemas.TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    tasks = crud_task.get_tasks_by_user(db, current_user.id)

    return tasks

@router.put("/{task_id}", response_model=task_schemas.TaskResponse)
def update_task(
    task_id: int,
    payload: task_schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    task = crud_task.get_task(db, task_id)

    if not task or task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    
    updated = crud_task.update_task(db, task, payload)

    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    
    task = crud_task.get_task(db, task_id)

    if not task or task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    
    crud_task.delete_task(db, task)