from jose import JWTError,jwt
from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import time
from datetime import datetime,timedelta

token_request=OAuth2PasswordBearer(tokenUrl='/login')
secret_pass='password'
alg='HS256'
time_s=33
def token_creator(dic:dict):
    bbc=dic.copy()
    
    time_measure= datetime.utcnow()+timedelta(minutes=time_s)
    bbc.update({'exp':time_measure})#we cant update on string so we need copy
    token_created=jwt.encode(bbc,secret_pass,algorithm=[alg])#we encode and passsed the token as string
    return  token_created
def token_decoder(des:str=Depends(token_request)):#token_request is the one to show login layout
    #if we dont vefiy by touching the token_request it wont show up
    cc=jwt.decode(des,secret_pass,algorithms=[alg])
    username=cc.get('username')
    
    return {'username':username}


def verfier(kk:str):
    def current_user(nam:dict=Depends(token_decoder)):
        if nam['username']!=kk:
            raise HTTPException(status_code=403,detail=('you are forbidden'))
        return nam['username']
    return current_user








