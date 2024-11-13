# Borrow from https://github.com/openai/swarm/blob/main/examples/basic/bare_minimum.py

from dotenv import load_dotenv
from swarm import Agent, Swarm

load_dotenv()

client = Swarm()

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
