import pandas as pd
import numpy as np
from fastapi import FastAPI
from sqlalchemy import MetaData,create_engine,Integer,String,Float,Column,ForeignKey,text
from sqlalchemy.orm import Session,declarative_base,sessionmaker,relationship
engine=create_engine('mysql+pymysql://root:password123@localhost/CORK')
session=Session(engine)
session.execute(text('DROP TABLE IF EXISTS student'))
session.commit()
session.execute(text('DROP TABLE IF EXISTS datascience'))
session.commit()
#reading=pd.read_sql('select * from weather_cast',engine)#just checking the sql in pandas
#print(reading)
base=declarative_base()
class University(base):
    __tablename__='datascience'
    faculty_id=Column(Integer,primary_key=True)
    course_name=Column(String(444))
    points=Column(Integer)
    year=Column(Integer)
    student=relationship('Student',back_populates='university')#so why used back_populates to access each other values
class Student(base):
    __tablename__='student'
    age=Column(Integer)
    boss_id=Column(Integer,primary_key=True)
    baito=Column(String(555))
    address=Column(String(555))
    student_id=Column(Integer,ForeignKey(University.faculty_id))#database rules to connect two tables
    university=relationship('University',back_populates='student')#so why we used th quotes because the University class maynot be created yet
base.metadata.create_all(engine)
session=Session(engine)
session.execute(text('INSERT INTO datascience(faculty_id,course_name,points,year) values(2,"socialinnovation",98,1)'))
session.commit()
Session=sessionmaker(bind=engine)
session=Session()
object1=University(course_name='db_course',points=88,year=1)

session.add(object1)
session.flush()
object2=Student(age=21,baito='staff',address='saitama',student_id=object1.faculty_id)
session.add(object2)
session.commit()
print(object2.university.course_name,object2.university.faculty_id,object2.university.points,object2.university.year)
print([x.baito for x in object1.student])
tra=pd.read_sql('SELECT * FROM DATASCIENCE',engine)
print(tra.columns)
print(tra.tail(44))
print(tra.isnull(),'if null then appear here')
print(tra.isnull().sum(),'if appears then come here')
print(tra[tra['faculty_id']<3][['course_name','year']])
print(object2.age)
print(object2.university)




    



