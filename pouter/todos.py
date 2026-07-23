from fastapi import APIRouter,FastAPI,HTTPException
from logger import ram
import logging
from keema import TodoCreate,TodoUpdate
app = FastAPI()
purpur=logging.getLogger(__name__)
pap=APIRouter(prefix='/podos/',tags=['ekaima'])

# Pydantic schema — defines shape of incoming data

todos = [
    {'id': 1, 'title': 'learn fastapi', 'done': False},
    {'id': 2, 'title': 'learn postgresql', 'done': False},
]

@pap.get('/')
def get_todos():
    purpur.info('fetching the data')
    return todos

@pap.get('/{todo_id}')
def get_todo(todo_id: int):
    
    for todo in todos:
        if todo['id'] == todo_id:
            purpur.info(f'fetching the data of {todo_id}')
            return todo
    purpur.warning('the data was never found')
    raise HTTPException (status_code=404,detail='error not found')

# now takes a Pydantic model instead of raw params
@pap.post('/',status_code=201)#we used status_code=201 usually 200 is shown on everyendpoints
#but when we do 201 it replies with created
def create_todo(todo: TodoCreate):
    new_todo = {
        'id': len(todos) + 1,
        'title': todo.title,   # access with dot notation
        'done': todo.done
    }
    todos.append(new_todo)
    purpur.info('just add the new data')
    return new_todo


# same here
@pap.put('/{todo_id}')
def update_todo(todo_id: int, updated: TodoUpdate):
    for todo in todos:
        if todo['id'] == todo_id:#we checked if todo[id] is = to pathparameter power of if..
            todo['title'] = updated.title
            todo['done'] = updated.done
            purpur.info(f'data added{todo_id}')
            return todo
    purpur.warning(f'yeah data not found{todo_id}')
    raise HTTPException (status_code=404,detail='detail not found')

@pap.delete('/{todo_id}')
def delete_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            purpur.info(f'data deleted{todo_id}')
            return {'message': 'deleted'}
    purpur.warning(f'detail not found{todo_id}')
    raise HTTPException (status_code=404,detail='no data found as you requested')