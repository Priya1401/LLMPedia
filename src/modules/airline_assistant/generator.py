from google import genai
from google.genai import types
from .prompts import system_message
from .tools import get_ticket_price

def ask_airline(client: genai.Client, model_name: str, user_input: str) -> str:
    # Start a chat session with automatic function calling enabled
    chat = client.chats.create(
        model=model_name,
        config=types.GenerateContentConfig(
            tools=[get_ticket_price],
            system_instruction=system_message,
        )
    )
    
    # Send the user message
    response = chat.send_message(user_input)
    
    # Return the text response
    return response.text
