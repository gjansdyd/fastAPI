#repository패턴
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database.orm import ToDo
from typing import List

def get_todos(session: Session) -> List[ToDo]:
    return list(session.scalars(select(ToDo)))

def get_todo_by_todo_id(session: Session, todo_id: int) -> ToDo | None:
    return session.scalar(select(ToDo).where(ToDo.id == todo_id))

def create_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo)
    session.commit() #저장이되는 시점
    session.refresh(instance=todo) #db에 저장된 todo불러오기 -> todo_id 값 알 수 있게 된다
    return todo

def update_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo)
    session.commit() #저장이되는 시점
    session.refresh(instance=todo) #db에 저장된 todo불러오기 -> todo_id 값 알 수 있게 된다
    return todo


def delete_todo(session: Session, todo_id: int) -> None:
    session.execute(delete(ToDo).where(ToDo.id == todo_id))
    session.commit() #auto commit을 false로 주었기 때문