from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class base(BaseModel):
    pass 

class register_class(base):
    course_name:str
    course_id:int
    day:str

