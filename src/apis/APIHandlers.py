from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
OAIkey = os.getenv("OAI")


client = OpenAI(api_key=OAIkey)

def Create_Assistant(name, instructions, tools, model):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model
    )


def Create_Thread():
    return client.beta.threads.create()

def New_Message(usermessage, threadID):
    return client.beta.threads.messages.create(
        thread_id=threadID,
        role="user",
        content=usermessage

    )
def Create_Run(threadID, AssistantID):
    return client.beta.threads.runs.create(
        thread_id=threadID,
        assistant_id=AssistantID,

    )
def Grab_Result(threadID, runID):
    received = False
    while not received:

        # Retrieve the latest run status
        results = client.beta.threads.runs.retrieve(
            thread_id=threadID,
            run_id=runID
        )

        # Check if the run is completed
        if results.status == 'completed':

            messages = client.beta.threads.messages.list(thread_id=threadID)
            for message in messages.data:
                role = message.role
                content = message.content[0].text.value
                received = True
                return f"Multichat: {content}"

def OpenRouterCall(model, uinput, chatid):
      print("todo")



#print(OpenAICall("gpt-4o", "What is the study of calculus"))

pmodel = "gpt-4o"
assistant = Create_Assistant("test", "Answer questions in a friendly but extremely information mannor", [{"type": "code_interpreter"}], pmodel)
thread = Create_Thread()
thread_id = thread.id
user_message = "Hello, how are you?"
New_Message(user_message, thread_id)
run = Create_Run(thread_id, assistant.id)
run_id = run.id  # Get the run ID from the returned object
result = Grab_Result(thread_id, run_id)
print(result)
