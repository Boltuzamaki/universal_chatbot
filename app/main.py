from fastapi import FastAPI
from database import create_tables
from routes import router
import uvicorn


app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup():
    create_tables()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)