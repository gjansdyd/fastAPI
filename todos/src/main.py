from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def health_check_handler():
    return {"ping": "pong"}


todo_data = {
    1: {
        "id": 1,
        "contents": "실전 FastAPI 섹션 0 수강",
        "is_done": True
    },
    2: {
        "id": 2,
        "contents": "실전 FastAPI 섹션 1 수강",
        "is_done": False
    },
    3: {
        "id": 3,
        "contents": "실전 FastAPI 섹션 2 수강",
        "is_done": False
    }
}


@app.get("/todos", status_code=200)
def get_todos_handler(order: str | None = None):
    ret = list(todo_data.values())
    if order == "DESC":
        return ret[::-1]
    return ret


@app.get("/todos/{todo_id}", status_code=200)
def get_todo_handler(todo_id: int):
    todo = todo_data.get(todo_id)
    if todo:
        return todo
    return HTTPException(status_code=404, detail="TODO not found")


class CreateToDoRequest(BaseModel):
    id: int
    contents: str
    is_done: bool


@app.post("/todos")
def create_todo_handler(request: CreateToDoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]


@app.patch("/todos/{todo_id}")
def update_todo_handler(todo_id: int,
                        is_done: bool = Body(..., embed=True)
                        ):
    todo = todo_data.get(todo_id)
    if todo:
        todo["is_done"] = is_done
        return todo
    return {}


@app.delete("/todos/{todo_id}", status_code=200)
def delete_todo_handler(todo_id: int):
    todo = todo_data.pop(todo_id, None)
    print(todo)
    if todo:
        return
    print("none")
    return HTTPException(status_code=404, detail="TODO not found")