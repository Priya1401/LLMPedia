from google import genai
from .prompts import system_message
from PIL import Image

def ask_chef(client: genai.Client, model_name: str, image: Image.Image, user_note: str = "") -> str:
    # Prepare prompt with optional user note
    prompt = "Here are my ingredients."
    if user_note:
        prompt += f" Note from me: {user_note}"
        
    # Generate content using the new client
    # config for system instruction if supported or prepend to prompt?
    # google-genai supports config=types.GenerateContentConfig(system_instruction=...)
    
    from google.genai import types
    
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt, image],
        config=types.GenerateContentConfig(
            system_instruction=system_message
        )
    )
    
    return response.text
