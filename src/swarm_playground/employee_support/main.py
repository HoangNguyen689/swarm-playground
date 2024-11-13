from dotenv import load_dotenv
from swarm import Swarm

from swarm_playground.employee_support.agent import operator_agent
from swarm_playground.employee_support.util import pretty_print_messages

load_dotenv()

client = Swarm()

messages = []
agent = operator_agent

while True:
    user_input = input("\033[90mUser\033[0m: ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(
        agent=agent,
        messages=messages,
    )

    pretty_print_messages(response.messages)

    messages.extend(response.messages)
    agent = response.agent
