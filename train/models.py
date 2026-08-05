from pydantic import BaseModel


base=BaseModel

class inserting_all(base):
    name:str
    age:int
    id:int

class not_at_all(base):
    name:str
    age:int
    id:int

class at_all(base):
    name:str
    age:int
    id:int



