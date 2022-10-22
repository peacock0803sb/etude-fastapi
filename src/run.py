from __future__ import annotations
import os
import logging

from etude_fastapi.main import app  # noqa


def handler(event, context):
    from mangum import Mangum

    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(event, context)


if __name__ == "__main__":
    from dotenv import load_dotenv

    import uvicorn

    load_dotenv()
    is_debug = os.environ.get("DEBUG", 0)
    log_level = "debug" if is_debug else "debug"
    logging.basicConfig(format="", level=logging.INFO if is_debug else logging.DEBUG)

    uvicorn.run(app, port=8080, log_level=log_level)
