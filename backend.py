from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Personal Finance Chatbot API",
    description="Provides budget summaries, spending insights, and AI-generated financial advice",
    version="1.0.0"
)

# Enable CORS for frontend (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, set your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routes
app.include_router(router)









