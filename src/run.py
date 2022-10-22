from __future__ import annotations
import os
import logging

from etude_fastapi.main import app  # noqa


def to_apigateway():
    from mangum import Mangum

    return Mangum(app, lifespan="off")


handler = to_apigateway()


if __name__ == "__main__":
    from dotenv import load_dotenv

    import uvicorn

    load_dotenv()
    log_level = "info" if os.environ.get("DEBUG", 0) else "debug"
    logging.basicConfig(level=logging.INFO if os.environ.get("DEBUG", 0) else logging.DEBUG)

    uvicorn.run(app, port=8080, log_level=log_level)
