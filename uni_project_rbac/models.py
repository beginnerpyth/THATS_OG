from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class base(BaseModel):
    pass 

class register_class(base):
    course_name:str
    course_id:int
    day:str

class student_register(base):
    student_name:str
    student_id:int
class student_update(base):
    student_name:str
    student_id:int
