# FASTAPI Imports
from fastapi import FastAPI, Request, Header, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from contextlib import asynccontextmanager
# Other Imports
from uuid import uuid4
from typing import Annotated, Union



# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup: Create database tables
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     asyncio.create_task(hit_loop())
#     yield


# Initialize FastAPI
app = FastAPI()
# Configuring templates directory for Jinja2
templates = Jinja2Templates(directory="templates")
items = []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/todos", response_class=HTMLResponse)
async def list_todos(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):
    if hx_request:
        return templates.TemplateResponse("todos.html", {"request": request, "todos": items})
    return JSONResponse(content=jsonable_encoder(items))


@app.post("/todos", response_class=HTMLResponse)
async def create_todo(request: Request, todo: Annotated[str, Form(...)]):
    items.append(TODO(todo))
    return templates.TemplateResponse("todos.html", {"request": request, "todos": items})


@app.put("/todos/{todo_id}", response_class=HTMLResponse)
async def update_todo(request: Request, todo_id: str, text: Annotated[str, Form()]):
    for index, todo in enumerate(items):
        if str(todo.id) == todo_id:
            todo.text = text
            break
    return templates.TemplateResponse(request=request, name="todos.html", context={"todos": items})


@app.post("/todos/{todo_id}/toggle", response_class=HTMLResponse)
async def toggle_todo(request: Request, todo_id: str):
    for index, todo in enumerate(items):
        if str(todo.id) == todo_id:
            items[index].done = not items[index].done
            break
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": items}
    )


@app.post("/todos/{todo_id}/delete", response_class=HTMLResponse)
async def delete_todo(request: Request, todo_id: str):
    for index, todo in enumerate(items):
        if str(todo.id) == todo_id:
            del items[index]
            break
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": items}
    )
# Todo Model


class TODO:
    def __init__(self, text: str):
        self.id = uuid4()
        self.text = text
        self.done = False


@app.get("/ping")
async def ping():
    print("Pong")
    return {"message": "pong"}


# TARGET_URL = "https://smart-attendance-system-sfho.onrender.com/ping"

# async def hit_loop():
#     """Background random ping task."""
#     async with httpx.AsyncClient() as client:
#         while True:
#             waiting=random.randint(40, 49)
#             print(f"Waiting self hit : {waiting} second")
#             await asyncio.sleep(waiting)
#             try:
#                 await client.get(TARGET_URL)
#             except Exception:
#                 pass




