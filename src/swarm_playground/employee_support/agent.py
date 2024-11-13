from swarm import Agent

operator_agent = Agent(
    name="Operator Agent",
    instructions="Determine which agent is best suited to handle the user's request, and transfer the conversation to that agent.",
)

email_agent = Agent(
    name="Email Agent",
    instructions="You are the email agent. You are responsible for write email requests.",
)

schedule_agent = Agent(
    name="Schedule Agent",
    instructions="You are the schedule agent. You are responsible for scheduling appointments.",
)


def transfer_back_to_operator():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return operator_agent


def transfer_to_email():
    return email_agent


def transfer_to_schedule():
    return schedule_agent


operator_agent.functions = [transfer_to_email, transfer_to_schedule]
email_agent.functions.append(transfer_back_to_operator)
schedule_agent.functions.append(transfer_back_to_operator)
