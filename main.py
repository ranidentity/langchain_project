
from langchain.schema import HumanMessage
from services.chat_services import ask_resume_chatbot


def run_interactive_chatbot():
    """Runs an interactive command-line interface for the resume chatbot."""
    print("\n--- Resume Chatbot (Powered by Groq) ---")
    print("Ask me anything about the resume (e.g., 'What is John's experience?', 'What skills does he have?').")
    print("Type 'exit' to quit.")

    while True:
        user_question = input("\nYour question: ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break

        response = ask_resume_chatbot(user_question)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    # If you were setting up a web framework (e.g., FastAPI):
    # from fastapi import FastAPI
    # app = FastAPI()
    # @app.post("/chat/")
    # async def chat_with_resume(request: ChatRequest): # Define ChatRequest Pydantic model
    #     response = ask_resume_chatbot(request.question)
    #     return {"answer": response}
    #
    # To run this example, just call the interactive function:
    run_interactive_chatbot()
