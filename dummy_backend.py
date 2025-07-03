from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Hello from backend"}


@app.get("/health")
def health():
    return {"status": "ok"}
