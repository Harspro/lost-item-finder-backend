from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# CORS Middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class ItemData(BaseModel):
    item: str
    lastSeen: str
    activity: str

@app.post("/find-item")
async def find_item(data: ItemData):
    possible_locations = [
        "Check under the sofa.",
        "Look in your pockets.",
        "Maybe you left it in the car?",
        "Did you check the kitchen counter?",
    ]
    return {"suggestion": random.choice(possible_locations)}
