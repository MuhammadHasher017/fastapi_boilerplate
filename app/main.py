
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import example
from app.core.middleware import add_logging_middleware

app = FastAPI(title="FastAPI V1 Example", version="1.0")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_logging_middleware(app)

app.include_router(example.router, prefix="/api/v1")

