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
    name:Optional[str]=None
    age:Optional[int]=None
    sex:Optional[str]=None
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
        return 'its already here'
    
    dic[id]=pp
    return dic[id]
@tr.put('/update-datas/{pa}')
def forreal(pa : int , jjk : slam):
    if pa not in dic:
     return {'error':'it doesnot  exist'}
    
    if jjk.name != None:
        dic[pa].name=jjk.name
    if jjk.age != None:
         dic[pa].age=jjk.age   
    if jjk.sex != None:
        dic[pa].sex=jjk.sex
    
    
    return dic[pa]




        
