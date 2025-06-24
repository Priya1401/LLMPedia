import json
from openai import OpenAI
from .prompts import (
    link_system_prompt,
    get_links_user_prompt,
    system_prompt,
    get_brochure_user_prompt
)

def get_links(openai: OpenAI, model: str, website):
    resp = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",  "content": link_system_prompt},
            {"role": "user",    "content": get_links_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(resp.choices[0].message.content)

def create_brochure(openai: OpenAI, model: str, company: str, url: str) -> str:
    prompt = get_brochure_user_prompt(company, url)
    resp = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt}
        ]
    )
    return resp.choices[0].message.content

def stream_brochure(openai: OpenAI, model: str, company: str, url: str, display_fn):
    prompt = get_brochure_user_prompt(company, url)
    stream = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt}
        ],
        stream=True
    )
    text = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        text += delta
        display_fn(text)
