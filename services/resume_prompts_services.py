from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

def _load_resume_content(file_path="prompts/my_resume.txt"):
    """Loads resume content from a specified text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Resume file '{file_path}' not found. Please create it.")
        return None
    except Exception as e:
        print(f"Error loading resume content from '{file_path}': {e}")
        return None
RESUME_CONTENT = _load_resume_content()

def _get_resume_chat_prompt_template(resume_text):
    """Returns a ChatPromptTemplate with the resume content embedded."""
    if not resume_text:
        # Fallback prompt if resume content isn't available
        return ChatPromptTemplate([
            ("system","You are a helpful AI assistant. You do not have specific resume data"),
            MessagesPlaceholder(variable_name="messages") 
        ])
    return ChatPromptTemplate([
        ("system","You are a helpful AI bot whose sole purpose is to answer questions about the provided resume content"),
        ("system","If the information is not explicitly stated in the resume, clearly state that you don't have that information"),
        ("system","Do not make up answers. Be concise and professional"),
        ("system",f"resume content: \n\n{resume_text}"),
        MessagesPlaceholder(variable_name="messages")
    ])

RESUME_CHAT_PROMPT = _get_resume_chat_prompt_template(RESUME_CONTENT)
