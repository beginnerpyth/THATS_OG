from databse import BaseMl
from databse import CaseML
from sqlalchemy import Integer,Table,Column,create_engine,String

class course_raw(BaseMl):
    c_name:str
    day:str

class student(BaseMl):
    student_name:str
    student_id:int
    subject:str

class grades(BaseMl):
    student_id:int
    subject:str


class course_toruoku(CaseML):
    __tablename__='classregister'
    c_name=Column(String,primary_key=True)
    day=Column(String)

class student_db(CaseML):
    __tablename__='student'
    student_name=Column(String)
    student_id=Column(Integer,primary_key=True)
    subject=Column(String)

class grades_touroku(CaseML):
    __tablename__='grades'
    student_id=Column(Integer,primary_key=True)
    subject=Column(String)




