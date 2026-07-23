from jose import JWTError,jwt
from fastapi import FastAPI,Request,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime,timedelta,timezone


alg='HS256'
secret_key='mypass'
time=20
def token_creator(email:str,role:str):
    data={'email':email,'role':role}
    copied_data=data.copy()
    copied_data.update({'exp':datetime.now(timezone.utc)+timedelta(minutes=time)})
    token_create=jwt.encode(copied_data,secret_key,algorithm=alg)
    return token_create

token_passer=OAuth2PasswordBearer(tokenUrl='/token/login')

def token_parser(data_str:str=Depends(token_passer)):
    real_data=jwt.decode(data_str,secret_key,algorithms=alg)
    email=real_data.get('email')
    role=real_data.get('role')
    if email  is None:
        raise HTTPException(status_code=401, 
                detail="Token payload is missing user data"
            )
    #alwasys use raise instead of return cause if its reutrn then at this time its none  and it returns raise 
    return {'email':email,'role':role}

def current_user_checker(name:str):
    def current_user_verfiy(role:dict=Depends(token_parser)):
        if role['role']!=name:
            raise HTTPException(status_code=403,detail=f'nope it doesnt match and only {name} can access it')
        return role
    return current_user_verfiy




