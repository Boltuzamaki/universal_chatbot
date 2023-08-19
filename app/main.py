import sys

sys.path.append(".")

from fastapi import FastAPI
from app.db.models import Base, create_engine
from app.core.config import settings
from app.api.api_router import api_router
import uvicorn

app = FastAPI()

app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
