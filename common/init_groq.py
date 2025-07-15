import os
from dotenv import load_dotenv
import getpass
from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel # Import BaseChatModel for type hinting
from common.settings import _groq_model_instance

load_dotenv()

def init_groq() -> BaseChatModel:
    if not os.environ.get("GROQ_API_KEY"):
        os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")
    groq_model_name = os.environ.get("GROQ_AI_MODEL", "mixtral-8x7b-32768") 
    try:
        model = init_chat_model(groq_model_name, model_provider="groq")
        print(f"Groq model '{groq_model_name}' initialized successfully.")
        return model
    except Exception as e:
        print(f"Error initializing Groq model '{groq_model_name}': {e}")
        # Depending on your application's needs, you might:
        # 1. Re-raise the exception: raise e
        # 2. Return None and handle it in the calling code
        # 3. Exit the program: sys.exit(1)
        return None # Or raise an error

_groq_model_instance = init_groq()