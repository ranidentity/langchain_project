import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage
from typing import List
from services.resume_prompts_services import RESUME_CHAT_PROMPT

load_dotenv()

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

model = init_chat_model(os.environ.get("GROQ_AI_MODEL"), model_provider="groq")


def get_resume_chatbot_chain():
    """Returns the Langchain chain for the resume chatbot."""
    if model and RESUME_CHAT_PROMPT:
        return RESUME_CHAT_PROMPT | model
    else:
        print("Chatbot chain cannot be initialized due to missing model or resume content.")
        return None
    
# def get_human_message(msg_list: List[str]) -> List[HumanMessage]:
#     messages = []
#     for msg in msg_list:
#         messages = HumanMessage(content=msg)

#     return messages

def ask_resume_chatbot(msg: List[BaseMessage]) -> str:
    """
    Sends a question to the resume chatbot and returns its response.
    """
    resume_chain = get_resume_chatbot_chain()
    if resume_chain:
        try:
            response = resume_chain.invoke({"messages": msg})
            return response.content
        except Exception as e:
            return f"An error occurred while processing your request: {e}"
    else:
        return "Chatbot service is not fully initialized. Please check configuration."