#again we are so disgusted but thing is veryhardgit
#yup here we are
#abhishek is undisputed king
#so what?so is everyonegit
from fastapi import FastAPI,Request
import logging
import time
from pouter import todos
from pouter import users
app=FastAPI()#we didnt even dologging.getlogger to track the file because logging.info we includes in line 15
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#so the level and format and filenam eare hardcoded mandatory variable we cant change it
app.include_router(todos.pap)#include_router is builtin function to extract that pap variable with it s endpoints 
app.include_router(users.bb)
@app.middleware('http')#its mandatory to write app.middleware and http inside it
async def sam(pagla:Request,call_next):#REquest and call_next are parameter we passed and with help of async we can use await
    start_time=time.time()#time to calculate current time
    resp=await call_next(pagla)#await python nativev language to wait for a sec and caall_next means execute the pagla i.e Request
    #so Request do is it track the user input and gives the endpoints
    duration=time.time()-start_time#again time to start subtract the value stored at start_time
    logging.info(f'{pagla.method} {pagla.url.path}-{resp.status_code}-{duration:.3f}s')#logging.info we can do it here too
    #there is rep.status_code not the pagla.status_code because status_code is always after the execution 
    return resp#no need to return logging cause it is automatically works and we returne resp


@app.get('/')
def show():
    return {'detail':'its working you see'}

