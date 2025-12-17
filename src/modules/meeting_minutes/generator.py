import tempfile
import os
from google import genai
from google.genai import types
from .prompts import system_prompt

def create_minutes(client: genai.Client, model_name: str, audio_file) -> str:
    # Save uploaded file to specific temp path to preserve extension
    suffix = os.path.splitext(audio_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(audio_file.getvalue())
        tmp_path = tmp.name

    try:
        # Upload to Gemini
        gemini_file = client.files.upload(path=tmp_path)
        
        # Prompt with the file
        response = client.models.generate_content(
            model=model_name,
            contents=[gemini_file, "Generate meeting minutes from this audio."],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        return response.text
    finally:
        # Cleanup local temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def stream_minutes(client: genai.Client, model_name: str, audio_file, display_fn) -> None:
    suffix = os.path.splitext(audio_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(audio_file.getvalue())
        tmp_path = tmp.name

    try:
        gemini_file = client.files.upload(path=tmp_path)
        
        response = client.models.generate_content_stream(
            model=model_name,
            contents=[gemini_file, "Generate meeting minutes from this audio."],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        
        text = ""
        for chunk in response:
            text += chunk.text
            display_fn(text)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
