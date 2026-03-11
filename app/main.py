from fastapi import FastAPI
from app.api.chat_api import router as chat_router
from app.api.faq_api import router as faq_router

app = FastAPI()

app.include_router(chat_router, prefix="/api")
app.include_router(faq_router, prefix="/api")   

@app.get("/")
def read_root():    
    return {"message": "Welcome to the AI Customer Support API!"}



