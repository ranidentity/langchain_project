
from langchain.schema import HumanMessage, BaseMessage, AIMessage
from services.chat_services import ask_resume_chatbot
from services.graph_builder import stream_graph_updates

def run_interactive_chatbot():
    """Runs an interactive command-line interface for the resume chatbot."""
    print("\n--- Resume Chatbot (Powered by Groq) ---")
    print("Ask me anything about the resume (e.g., 'What is John's experience?', 'What skills does he have?').")
    print("Type 'exit' to quit.")

    conversation_history: list[BaseMessage] = []
    while True:
        user_input_string = input("\nYour question: ")
        if user_input_string.lower() == 'exit':
            print("Goodbye!")
            break
        user_message_object = HumanMessage(content=user_input_string)
        conversation_history.append(user_message_object)

        response_content = ask_resume_chatbot(conversation_history)

        ai_message_object = AIMessage(content=response_content)
        conversation_history.append(ai_message_object)

        print(f"Chatbot: {response_content}")



def langgraphchatbot():
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input)
            break


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
    # run_interactive_chatbot()
    langgraphchatbot()

