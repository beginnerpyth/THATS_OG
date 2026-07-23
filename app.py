from fastapi import FastAPI
from database import engine, Base
from routers import lost, found, claims

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lost & Found")

app.include_router(lost.router, prefix="/lost", tags=["Lost Items"])
app.include_router(found.router, prefix="/found", tags=["Found Items"])
app.include_router(claims.router, prefix="/claims", tags=["Claims"])

@app.get("/")
def root():
    return {"message": "Lost & Found API running"}