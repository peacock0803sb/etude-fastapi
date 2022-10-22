from logging import getLogger

from fastapi import FastAPI

from etude_fastapi.models import Contact

app = FastAPI()
logger = getLogger(__name__)


@app.get("/")
async def root():
    return {"message": "hello!"}


@app.post("/contact")
async def contact(data: Contact):
    logger.info("data: %s", data)
    return {"message": "success!", "body": {}}
