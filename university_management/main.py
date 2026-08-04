from fastapi import FastAPI,HTTPException,Request
from routes import router
from fastapi.staticfiles import StaticFiles
import uploadfile
import logging
import time
from databse import eng,CaseML


app=FastAPI()
app.include_router(router)
app.mount('/nandemo',StaticFiles(directory='fupload'),name='kuchbi')
app.include_router(uploadfile.shouter)
CaseML.metadata.create_all(bind=eng)

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(filename)s-%(name)s-%(message)s')

@app.get('/')
def home():
    return 'you are home'
@app.middleware('http')
async def mid(req:Request,call_next):
    start_time=time.time()
    resp=await call_next(req)#here req and resp are not same
    #req contains the request paths and resp contains the response after it
    stop_time=time.time()-start_time
    logging.info(f'{req.url.path}-{resp.status_code}-{req.method}={stop_time:3f}s')
    return resp











