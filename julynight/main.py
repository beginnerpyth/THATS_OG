from fastapi import FastAPI,HTTPException,Request
import routes
from fastapi.staticfiles import StaticFiles
from datetime import datetime,timedelta
import fileuploads
import time
import logging
app=FastAPI()


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(name)s-%(message)s')#this is before
#the requests and middleware
app.mount('/fileuploader',StaticFiles(directory='filestorer'),name='you_can_name_anything')
app.include_router(routes.router)
app.include_router(fileuploads.kouter)



@app.get('/')
def home():
    return 'home sweet home'

@app.middleware('https')
async def no_trespas(checker:Request,call_next):#requests have method because of http

    start_time=time.now()
    if checker.url.path in ['/','/get']:
        return await call_next(checker)
    logging.basicConfig(logging.debug,)
    api_key=checker.headers.get('same_api')
    if api_key != 'mypassa':
        raise HTTPException(detail='no header no trespassing')
    

    resp= await call_next(checker)#freeze everything and when someone request the endpoint 
    #it returns the status_code
    stop_time=start_time-time.now()
    logging.info(f'{checker.url.path},{checker.headers.get("bearer")},{checker.method},{resp.status_code},{stop_time}')
    return f'{resp}"time_it_took":{stop_time}'


    
    