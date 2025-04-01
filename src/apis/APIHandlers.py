from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OAIkey = os.getenv("OAI")


client = OpenAI(api_key=OAIkey)

def OpenAICall(model, uinput):
    response = client.responses.create(
        model=model,
        input= uinput
    )
    return response.output_text


print(OpenAICall("gpt-4o", "What is the study of calculus"))
