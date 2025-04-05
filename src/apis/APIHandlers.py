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
    return response.output_text

def Create_Thread():
    return client.beta.threads.create()

def OpenRouterCall(model, uinput, chatid):
      print("todo")


#print(OpenAICall("gpt-4o", "What is the study of calculus"))
