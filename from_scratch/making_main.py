from fastapi import FastAPI,APIRouter,HTTPException,Request
import logging
import time
from schema import create_user


logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(name)s-%(message)s")


app=FastAPI()

@app.middleware('http')
async def pr(data:Request,call_next):
    start_tt=time.time()
    resp=await call_next(data)
    stop_tt=start_tt-time.time()
    logging.info(f'%{data.method}s-%{data.url.path}s-%{data.url}s-%{resp.status_code}s-%{stop_tt}s')
    return resp




@app.get('/')
def for_real():
    return ('welcome to my page')




