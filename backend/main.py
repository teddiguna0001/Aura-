import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
load_dotenv()
app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_methods=['*'],allow_headers=['*'])
client=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
class ChatRequest(BaseModel):
    message:str
@app.post('/api/chat')
def chat(request:ChatRequest):
    response=client.models.generate_content(model='gemini-3.5-flash',contents=request.message)
    return {'reply':response.text}
