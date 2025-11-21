from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello Feyza! Your GET endpoint works 🎉"}
