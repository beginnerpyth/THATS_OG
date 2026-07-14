from pydantic import BaseModel
class TodoCreate(BaseModel):
    title: str
    done: bool = False  # default is False, so optional to send

class TodoUpdate(BaseModel):
    title: str
    done: bool

class users_signup(BaseModel):
    email:str
    password:str
class users_login(BaseModel):
    email:str
    password:str
class users_verify(BaseModel):
    acess_token:str
    token_type:str='bearer'



