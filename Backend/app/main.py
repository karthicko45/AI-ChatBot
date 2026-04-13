from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chats import router as chat_router

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Ollama Backend Running 🚀"}