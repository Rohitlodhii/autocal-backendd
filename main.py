from contextlib import asynccontextmanager
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from constants import SERVER_URL , PORT , ENV 

from apps.calculator.route import router as calculator_router

@asynccontextmanager
async def lifespan (app : FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

#Setting up the Cors middleware and allowing all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://autocalai.vercel.app",
        "https://autocal-nv6ix5cze-rohitlodhiis-projects.vercel.app",
        "https://autocal-rohitlodhiis-projects.vercel.app"
    ],  # Only allow this specific origin
    allow_credentials=True,
    allow_methods=["*"],  # You can adjust this based on the methods you want to allow (GET, POST, etc.)
    allow_headers=["*"]
)

@app.get("/")
async def health():
    return {'message':"Server is Running"}


app.include_router(calculator_router , prefix="/calculate" , tags=['calculate'])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=PORT, reload=(ENV == "dev"))
