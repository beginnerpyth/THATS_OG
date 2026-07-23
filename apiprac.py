from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional

tr=FastAPI()
dic={1:{'name':'ram',
         'age':13,
         'sex':'M'
         }}
class kaka(BaseModel):#name and age is like paramaters so we didint use ""
    name:str
    age:int
    sex:str
class slam(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    sex:Optional[str] = None
@tr.get('/new again')
def ram():
    return {'man':'steel'}

@tr.get('/dicitonartry/{past_id}')#so this one is path parameter 
def foreal(past_id:int=Path(...,description='you must pass the value',gt=0,lt=10)):#... means must pass the value
    if  past_id in dic:
        return dic[past_id]
    return {'error':'the data you want to search is not found'}
@tr.post('/posting-datas/{id}')
def post(id:int,pp:kaka):
    if id in dic:
        return 'its already here'#returns means dont execute after this 
    
    dic[id]=pp#its means if not in dic then execute from here
    return dic[id]
@tr.put('/update-datas/{pa}')
def forreal(pa : int , jjk : slam):#its like jjk calling slam asks the user a input
    if pa not in dic:
     return {'error':'it doesnot  exist'}
    
    if jjk.name !=None:
        dic[pa].name = jjk.name
    if jjk.age !=None:
         dic[pa].age = jjk.age   
    if jjk.sex !=None:
        dic[pa].sex = jjk.sex
    
    
    return dic[pa]
@tr.delete('/for-deleting/{sa}')
def deleting(sa:int):
    if sa not in dic:
        return {'error':'its not here'}
    del dic[sa]#it executes and return the message
    return{'message':'its deleted'}





        
