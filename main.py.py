from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ItemData(BaseModel):
    item: str
    lastSeen: str
    activity: str

suggestions = [
    "Check under the sofa.",
    "Look in your pockets.",
    "Maybe you left it in the car?",
    "Did you check the kitchen counter?",
    "Look near where you usually keep similar items.",
    "Check your bag or backpack."
]

@app.post("/find-item")
async def find_item(data: ItemData):
    suggestion = random.choice(suggestions)
    return {"suggestion": suggestion}