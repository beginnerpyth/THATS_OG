from fastapi import FastAPI
import routes
app=FastAPI()
app.include_router(routes.router)
@app.get('/')
async def home():
    return 'its home'