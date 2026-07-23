from fastapi import FastAPI
import routes

app=FastAPI()

app.include_router(routes.router)

@app.get('/')
def home():
    return 'home sweet home'