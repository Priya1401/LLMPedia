import json
from google import genai
from google.genai import types
from .prompts import (
    link_system_prompt,
    get_links_user_prompt,
    system_prompt,
    get_brochure_user_prompt
)
from .website import Website

def get_links(client: genai.Client, model_name: str, website_url: str):
    website = Website(website_url)
    response = client.models.generate_content(
        model=model_name,
        contents=get_links_user_prompt(website),
        config=types.GenerateContentConfig(
            system_instruction=link_system_prompt,
            response_mime_type="application/json"
        )
    )
    return json.loads(response.text)

def create_brochure(client: genai.Client, model_name: str, company: str, url: str) -> str:
    prompt = get_brochure_user_prompt(company, url)
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def stream_brochure(client: genai.Client, model_name: str, company: str, url: str, display_fn):
    prompt = get_brochure_user_prompt(company, url)
    response = client.models.generate_content_stream(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )
    
    text = ""
    for chunk in response:
        text += chunk.text
        display_fn(text)
