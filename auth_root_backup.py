from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta

pwd=CryptContext(schemes='bcrypt',deprecated='auto')
def pass_in(passw:str):
    return pwd.hash(passw)
def pass_check(plain_pass:str,hashed:str):
    return pwd.verify(plain_pass,hashed)

secret_pass='wewewe'
algorithm='HS256'
expire_token=30
def creation(data:dict):
    copy_data=data.copy()
    time_up=datetime.utcnow()+timedelta(minutes=expire_token)
    pp=copy_data.update({'exp':expire_token})
    jwt_encode=jwt.encode(pp,expire_token,algorithm=algorithm)
    return jwt_encode
