
# from uuid import uuid4

# class TODO:
#     def __init__(self,text:str):
#         self.id = uuid4()
#         self.text=text
#         self.done = False


# y=[]

# while True:
#     x=TODO(input())
#     y.append(x.id)
#     print(y)


# from fastapi.encoders import jsonable_encoder
# from datetime import datetime
# from uuid import uuid4

# data = {"id": uuid4(), "created": datetime.now()}
# print(jsonable_encoder(data))


# from fastapi import FastAPI, Request, Header
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from typing import Annotated, Union
# import time


# temp1 = Jinja2Templates(directory='temp1')

# app = FastAPI()


# @app.get("/", response_class=HTMLResponse)
# async def index():
#     return temp1.TemplateResponse(name='HTMX.html')

# @app.get("/test",response_class=HTMLResponse)
# async def home(request: Request):
#     # time.sleep(2)
#     return temp1.TemplateResponse(request=request,name='response.html')




from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='temp1')
items = []


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/todos', response_class=HTMLResponse)
async def list_items(request: Request,):
    return templates.TemplateResponse('todos.html', {'request': request, 'items': items})


@app.post('/todos', response_class=HTMLResponse)
async def create_list(request:Request, name: str = Form(...)):
    items.append(name)
    return templates.TemplateResponse('todos.html', {'request': request, 'items': items})



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('test:app', port=8002, reload=True)
