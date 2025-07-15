from fastapi import FastAPI

app = FastAPI()

@app.post("/chat/")
async def chat_with_resume(request: ChatRequest): # Define ChatRequest Pydantic model
    response = ask_resume_chatbot(request.question)
    return {"answer": response}