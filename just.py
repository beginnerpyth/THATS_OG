from fastapi import FastAPI,Path#path means we can give details to path parameter 
from typing import Optional
from pydantic import BaseModel
sap=FastAPI()
geda={ 1:{'name' : 'japanese',
         'age' : 400,
         'sex':'F'}
         }
class copy(BaseModel):
   name:str
   age:int
   sex :str
class li(BaseModel):
  name:Optional[str]=None
  age:Optional[int]=None
  sex:Optional[str]=None
@sap.get('/get/details/')
def lim():
    return {'name':'first_data'}
@sap.get('/get/names/{geda_id}')#geda_id is path paremeter because we defined in url and in mag function
def mag(geda_id:int=Path(...,description='you need to insert the id',gt=0,lt=4)):#... means none and able to
 #description and all those
 return geda[geda_id]# so it automatically gives us error if there is not data
@sap.get('/get/allnames/')
def rag(herum : int,exo:Optional[str]= None):#query parameter cause we dont specify in url
   #note that we did herum : int at first because if dont do that then we need to set none evrything 
   #that comes after optional set to nine
   for id in geda:
      if geda[id]['name']==exo:#so it means 
        return geda[id]
      return 'data is empty'
#combining path and query parameter

@sap.post('/combining/{geda_id}')
def combine(geda_id:int,milxa:copy):#so we did milxa:copy because for basemodel referneces
 if geda_id in geda:
   return {'its already there'}
 geda[geda_id]=milxa#milxa ma xa class and three parameter
 return geda[geda_id]

#put method used to update things
@sap.put('/get-update/{id}')
def update(id:int,chor:li):#we used li cause when we send tyhe only name then pothers remains same
  if id not in geda:#so we pass 1 which will execute error and end
    return {'error':'it doesnt exist'}
  if chor.name != None:#so we pass 2 and we went to this one and we dont do anything cause name is already
    #saved from beginning and saves again if its not equals to none
    geda[id].name=chor.name
  if chor.age != None:#same like above explanantion
    geda[id].age=chor.age
  if chor.sex != None:
    geda[id].sex=chor.sex
  #geda[id]=chor#geda[id]=chor it is dicitionary method so it means add geda[newid]=values
  return geda[id]#if everything is none then return old data
#delete method 
@sap.delete('/to-delete/{i}')#we cant use the space in url mind it
def delete(i:int):
  if i not in geda:
    return{'errir':'it doesnt exist'}
  del geda[i]#del is magiuc that deletes 
  return{'message':'deleted succesfully'}

   
