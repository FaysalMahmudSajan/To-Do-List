
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')
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
    uvicorn.run('main:app', port=8002, reload=True)

