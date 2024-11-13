import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def get_temperature(location: str):
    """
    Get the temperature of a specific location
    """
    if location == "Tokyo":
        return 18
    elif location == "Hanoi":
        return 25

    return 20


tool_schemas = [
    {
        "type": "function",
        "function": {
            "name": "get_temperature",
            "description": "Get the temperature of a specific location",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string"}},
                "required": ["location"],
            },
        },
    }
]


SYSTEM_PROMPT = "You are a helpful customer support assistant. Use the supplied tools to assist the user."


messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


def run_continuously(messages):
    num_init_messages = len(messages)
    messages = messages.copy()

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tool_schemas,
        )

        message = response.choices[0].message
        messages.append(message)

        if message.content:
            print(f"Bot:", message.content)

        if not message.tool_calls:
            break

        tool_call = response.choices[0].message.tool_calls[0]
        arguments = json.loads(tool_call.function.arguments)
        location = arguments.get("location")

        print(f"Bot: Using", tool_call.function.name, "with location", location)

        temperature = get_temperature(location)

        result_message = {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(
                {
                    "location": location,
                    "temperature": temperature,
                }
            ),
        }
        messages.append(result_message)

    return messages[num_init_messages:]


while True:
    user_input = input("\033[90mUser\033[0m: ")
    messages.append({"role": "user", "content": user_input})

    new_messages = run_continuously(messages)
    messages.extend(new_messages)
