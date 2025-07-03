from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Epic Custom Load Balancer")

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Epic Load Balancer is running!"}
