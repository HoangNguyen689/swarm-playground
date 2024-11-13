from typing import Optional

from pydantic import BaseModel


class Agent(BaseModel):
    name: str = "Agent"
    model: str = "gpt-4o-mini"
    instructions: str = "You are a helpful Agent"
    tools: list = []


class Response(BaseModel):
    agent: Optional[Agent]
    messages: list
