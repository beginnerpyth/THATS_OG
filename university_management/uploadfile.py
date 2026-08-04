from fastapi import FastAPI,HTTPException,UploadFile,File,APIRouter
from fastapi.staticfiles import StaticFiles
import os



shouter=APIRouter()
os.makedirs('fupload',exist_ok=True)
@shouter.post('/upload_file')
def upload_file(irete:UploadFile=File(...)):
    image_type=['image/heic','image/png','image/jpeg']
    if irete.content_type not in image_type:
        return 'corrupted image type'
    total_size=irete.file.read() 
    if len(total_size) > 3000*1024:
        return 'its bigger than 3000kb'
    file_path=f'fupload/{irete.filename}'
    with open(file_path,'wb')as f:
        f.write(total_size)
    return f'the file has been uploaded {irete.filename}'







