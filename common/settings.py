import os
from dotenv import load_dotenv

# Load environment variables FIRST and ONLY ONCE
# This ensures that any subsequent imports that rely on these env vars
# will find them already loaded.
load_dotenv()

_groq_model_instance = None
