import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION"),
)


@app.get("/")
def index():
    return {
        "status": "success",
        "message": f"{os.getenv('APP_NAME')} - v{os.getenv('APP_VERSION')}"
    }
