from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta
from pouter.users import User,UserRole

bbc=CryptContext(schemes=['bcrypt'],deprecated='auto')
def hashpass(bass:str):
    return bbc.hash(bass)
def hasverify(tasikame:str,sas:str):
    return bbc.verify(tasikame,sas)

alpass='jjk'
exp_token=50
alg='HS256'

def jwt_te(po:dict):
    data_copy=po.copy()
    tim_e=datetime.utcnow() + timedelta(minutes =exp_token)
    data_copy.update({'exp':tim_e})
    jw_en=jwt.encode(data_copy,alpass,algorithm=alg)#it hands down to user browserse
    return jw_en
def err_ch(so:str):
    try:
        token_s=jwt.decode(so,alpass,algorithms=[alg])
        bb=token_s.get('sub')
        if bb is None:
            return None
        return bb
    except JWTError:
        return None
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# when creating token, include role
token = create_access_token({
    'sub': user.email,
    'role': user.role  # add role here
})


