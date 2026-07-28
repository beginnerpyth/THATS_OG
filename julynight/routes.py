from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI,Depends,Request,APIRouter,HTTPException,Response,Header
from auth import  token_creator,token_parser,current_user_checker
from services import secondfloor
from database import settings,get_db
from models import User
from sqlalchemy.orm import Session
router=APIRouter()
papa=secondfloor()
@router.post('/token/login')
def login(formfiller:OAuth2PasswordRequestForm=Depends()):#so OAuth2PasswordRequestForm makes login buttons
    #and its a class so we can even access it like dot notation and insert into depends
    if formfiller.username=='admin' and formfiller.password=='admin123':
        token=token_creator('hseee55@gmail.com','admin')
        return {'access_token':token,'token_type':'bearer'}
    if formfiller.username == 'user' and formfiller.password == 'user123':
        token=token_creator('user7779@gmail.com','user')
        return {'access_token':token,'token_type':'bearer'}
    raise HTTPException (status_code=401,detail=f'you are forbidden as{formfiller.username}')

#just making endpoints
@router.get('/admin')
def admin(response:dict=Depends(current_user_checker('admin'))):
    return f'here only {response} can access it'

@router.get('/user')
def user(response:dict=Depends(current_user_checker('user'))):
    return f'here only {response} access it'

@router .get('/peter')
def current_user(response:dict=Depends(token_parser)):
    return response


@router.get('/all_data')
def get_all(id:int):
    return papa.get_user_by_id(id)

@router.put('/update_user')
def update_user(name:str,id:int,role:str):
    return papa.update_user(name,id,role)

@router.post('/add_user')
def create_user(name:str,id:int,role:str,email:str):
    return papa.create_user(name,id,role,email)

@router.get('/users')
def get_users(
    page: int = 1,
    limit: int = 10,
    search: str | None = None,
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    
    query = db.query(User)
    
    # filter by search if provided
    if search:
        query = query.filter(User.name.contains(search))
    
    total = query.count()
    users = query.offset(skip).limit(limit).all()
    
    return {
        'page': page,
        'limit': limit,
        'total': total,
        'total_pages': total // limit,
        'has_next': (page * limit) < total,
        'has_previous': page > 1,
        'data': users
    }

@router.get('/headers')
def set_headers(resp:Response,suleman:str=Header(...)):#if header mismatched with suleman
    #it rejects and doesnt even execuete if statement
    if suleman != 'your_man':#every request there is header 
        raise HTTPException (detail='header didnt matched')

    resp.headers['papapa']='timewill'
    resp.headers['human']='beingmustmaster'

    return f'{suleman} here you are allowed'



