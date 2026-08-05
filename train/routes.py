from fastapi import FastAPI,HTTPException,Depends,Request,APIRouter
from jose import jwt
from models import inserting_all,not_at_all,at_all
router=APIRouter(prefix='/hey',tags=['/gotaanno'])
fake_database={1:{'id':1,'name':'abhishek','age':22}}
@router.get('/get')
def fetch():
    return 'welcome'

@router.get('/fetch_all')
def fetch_all(id:int):
    if id in fake_database:
        return fake_database[id]
    return 'there is no data'


@router.post('/insert_all')
def post_all(forme:inserting_all,id:int):
    if id in fake_database:
        return 'already saved' 
    fake_database[id]=forme
    

    return fake_database

@router.put('/updating__data')
def put_all(hermes:not_at_all):
    if id in fake_database['id']:
        fake_database[id]=not_at_all
    return 'there is no data'












