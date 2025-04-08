from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
import json
from src.backend import UserSaves as US

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
                return f"Multichat,: {content}"

def OpenRouterCall(model, uinput, chatid):
      print("todo")

def RunChat(model, provider):
    if provider == "openai":
        data = US.load_json_file("openai.json")
        print("[DEBUG] Contents of openai.json:", data)
        global assistainid
        assistainid = None

        for key, value in data.items():
            if value.strip().lower() == model.strip().lower():  # 🛠 robust match
                print(f"Found {model} with key {key}")
                assistainid = key
                break

        if assistainid is None:
            print(f"Model '{model}' not found in openai.json.")
            print("Available models:", ", ".join(data.values()))
            return

        thread_id = US.CreateUser()
        user_message = input("Chat With AI: ")
        New_Message(user_message, thread_id)
        run = Create_Run(thread_id, assistainid)
        result = Grab_Result(thread_id, run.id)
        print("Model:", model, result)







    elif provider == "openrouter":
        print("todo")



