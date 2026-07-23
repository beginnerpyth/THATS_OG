from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import HTMLResponse
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Global mock datasets
c = [{'name': 'ww', 'id': 2, 'grade': 'rr', 'year': 'tt'}]

@app.get('/dd', include_in_schema=False)
async def root():
    return 'you are at home'

# Combined or distinct home paths
@app.get('/home', response_class=HTMLResponse, include_in_schema=False)
@app.get('/posts', response_class=HTMLResponse, include_in_schema=False)
async def html_tey():
    return '<h1>HTMLhok</h1>'

@app.get('/decor')
async def fahh(name: Optional[str] = None):
    return f'my name is {name}'

# Moved this route to '/headers' so it doesn't conflict with '/'
@app.get('/headers')
async def get_header(accept: str = Header(None), content_type: str = Header(None)):
    return {
        'accept': accept,
        'content_type': content_type
    }

class FilterPut(BaseModel):
    name: str
    id: int
    grade: str

@app.get('/filtering_data', response_model=FilterPut)
async def filter_out(id: int):
    for t in c:
        if id == t['id']:
            return t
    raise HTTPException(status_code=404, detail='not found')

@app.get('/users')
def get_users(page: str, limit: str):
    return {'page': page, 'limit': limit}

@app.get('/ousers')
def get_ousers(page: int = 1, limit: int = 10, search: Optional[str]= None):
    # 1. Start with the whole list
    filtered_users = c

    # 2. Correct search loop filtering through dictionaries
    if search:
        filtered_users = []
        for user in c:
            if search.lower() in user['name'].lower():
                filtered_users.append(user)
                
    # 3. Correct pagination math formula
    start = (page - 1) * limit
    end = start + limit
    
    # 4. Return results safely with len() function syntax
    return {
        'page': page,
        'limit': limit,
        'total': len(filtered_users),
        'kk': filtered_users[start:end]
    }
