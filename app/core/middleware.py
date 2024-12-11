
from fastapi import FastAPI, Request
import logging

def add_logging_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        logging.info(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        return response

