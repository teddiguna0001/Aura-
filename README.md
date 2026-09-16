# AURA

API Integrated chatbot from Gemini API Key.

A small chatbot with a static frontend and FastAPI backend powered by the Google Gemini API.

## Run

1. Add GEMINI_API_KEY to a local .env file.
2. Install dependencies: pip install -r requirements.txt
3. Backend: uvicorn backend.main:app --reload --port 8000
4. Frontend: python -m http.server 5500 --directory frontend

The .env file is excluded from Git.
