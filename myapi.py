from just import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students={1:{'name':'john','age':17,'grade':'year 12'}}
class k(BaseModel):
    name:str
    age:int
    grade : str
class m(BaseModel):
    name:Optional[str]=None
    age: Optional[int] = None
    grade : Optional[str]= None
@app.get("/")
def index():
    return {'name':'first data'}
@app.get('/get-student/{student_id}')
def get_students(student_id:int = Path(..., description = 'the id of the student you want to view',gt = 0,lt = 3)):
    return students[student_id]
@app.get('/get-by-name/{i}') 
def get_yo(*,i: int ,name: Optional[str]= None,test : int):
    for i in students:
        if students[i]['name']==name:
           return students[i]
    return {'data':'not found'} 
@app.post('/get-baba/{student_id}')
def sir(student_id:int,studs:k):
    if student_id in students:
        return ('its already there')
    students[student_id] = studs
    return students[student_id]
@app.put('/update-student/{student_id}')
def update_student(student_id :int , studs : m):
    if student_id not in students:
        return ' it doesnt even exist'
    if studs.name != None:
     students[student_id].name = studs.name
    if studs.age!= None:
      students[student_id].age=studs.age
    if studs.grade != None:
        students[student_id].grade= studs.grade
    
    
    return students[student_id]

