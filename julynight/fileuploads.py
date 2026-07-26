from fastapi import APIRouter,FastAPI,HTTPException,UploadFile,File
import pytest
from typing import List
import os
import shutil

kouter=APIRouter()
os.makedirs('filestorer',exist_ok=True)
file_store=[]

@kouter.post('/zara')
def file_uploads(file:UploadFile=File(...)):#we use[] instead of () because () converts into list while [] label as list but doesnt
    #convert the data
    
    allowed_types=['image/jpeg','image/mov','image/heic','image/png']
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400,detail='the image type is invalid')

    contents=file.file.read()
    if len(contents) > 2 * 1024 * 1024:
        raise HTTPException(status_code=400,detail='size too big')

    file_saver=f'filestorer/{file.filename}'
    with open (file_saver,'wb') as f:
        f.write(contents)
        file_store.append(file.filename)

    return {'file_name':file.filename,'file_type':file.content_type,'filename':file_store}
    





