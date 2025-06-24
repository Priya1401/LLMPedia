from .tools import transcribe_audio
from .prompts import system_prompt, get_minutes_user_prompt

def create_minutes(openai, model: str, audio_file) -> str:
    # 1) get transcript
    transcript = transcribe_audio(openai, audio_file)

    # 2) generate minutes
    resp = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",  "content": system_prompt},
            {"role": "user",    "content": get_minutes_user_prompt(transcript)}
        ]
    )
    return resp.choices[0].message.content

def stream_minutes(openai, model: str, audio_file, display_fn) -> None:
    transcript = transcribe_audio(openai, audio_file)
    stream = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",  "content": system_prompt},
            {"role": "user",    "content": get_minutes_user_prompt(transcript)}
        ],
        stream=True
    )
    text = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        text += delta
        display_fn(text)
