from fastapi import FastAPI
import routes
from fastapi.staticfiles import StaticFiles
import fileuploads
app=FastAPI()

app.mount('/fileuploader',StaticFiles(directory='filestorer'),name='you_can_name_anything')
app.include_router(routes.router)
app.include_router(fileuploads.kouter)

@app.get('/')
def home():
    return 'home sweet home'
