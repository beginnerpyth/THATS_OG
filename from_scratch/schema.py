from pydantic import BaseModel




class create_user():
    id:int
    name:str
    email:str
class update_user():
    id:int
    name:str
    email:str


class user_sign(BaseModel):
    email:str
    password:str
class user_login(BaseModel):
    email:str
    password:str
