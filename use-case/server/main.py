import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers.main_router import router as api_router
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)