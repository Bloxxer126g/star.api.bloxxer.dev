from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

current_colour = {"colour": "#ffffff"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/colour.json")
async def get_colour():
    return current_colour

@app.patch("/api/colour.json")
async def update_colour(data: dict):
    global current_colour
    current_colour = data
    print("Updated colour:", current_colour)
    return {"ok": True}
