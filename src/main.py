from fastapi import FastAPI
from rutes.rute import router
from Database_config.config import engine
from Database_config import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
