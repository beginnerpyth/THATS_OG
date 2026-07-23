from jose import JWTError,jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime,timedelta
dam=CryptContext(['bcrypt'],deprecation='auto')

def hash_password(passe:str):
    
    tr=dam.hash(passe)
    return tr
def verfiy_has(passe:str):
    vr=dam.verfiy(passe,hash_password)

exp_t=30
sec_pass='another_love'
alg='HS256'

def en_c(pp:dict):
    dat=pp.copy()
    tim=datetime.utc()+timedelta(minutes=exp_t)
    dat.update({'exp':tim})
    jw=jwt.encode(dat,sec_pass,algorithm=alg)
    return jw
def en_v(ps:str):
    sap=jwt.decode(ps)
    sap_chech=sap.get({'sub'})
    if sap_chech is None:
        return JWTError
    return sap_chech










