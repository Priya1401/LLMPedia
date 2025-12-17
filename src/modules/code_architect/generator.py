from google import genai
from google.genai import types
from .prompts import system_message

def architect_review(client: genai.Client, model_name: str, code_snippet: str) -> str:
    # Generate content
    response = client.models.generate_content(
        model=model_name,
        contents=code_snippet,
        config=types.GenerateContentConfig(
            system_instruction=system_message
        )
    )
    
    return response.text
