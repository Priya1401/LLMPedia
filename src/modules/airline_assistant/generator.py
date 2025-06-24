import json
from openai import OpenAI

from .prompts import system_message, function_spec
from .tools import get_ticket_price

def ask_airline(openai: OpenAI, model: str, user_input: str) -> str:
    # 1) initial user + system
    messages = [
        {"role": "system",  "content": system_message},
        {"role": "user",    "content": user_input}
    ]

    # 2) call with function spec
    resp = openai.chat.completions.create(
        model=model,
        messages=messages,
        functions=[function_spec],
        function_call="auto"
    )
    msg = resp.choices[0].message

    # 3) if the model wants to call our tool:
    if msg.function_call:
        args = json.loads(msg.function_call.arguments)
        result = get_ticket_price(**args)

        # append the function call and response
        messages.append({
            "role": "assistant",
            "content": None,
            "function_call": {
                "name": msg.function_call.name,
                "arguments": msg.function_call.arguments
            }
        })
        messages.append({
            "role": "function",
            "name": msg.function_call.name,
            "content": json.dumps(result)
        })

        # 4) second request to let the model finish the answer
        followup = openai.chat.completions.create(
            model=model,
            messages=messages
        )
        return followup.choices[0].message.content

    # 5) otherwise just return what it said
    return msg.content
