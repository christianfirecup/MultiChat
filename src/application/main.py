import json
import os
from src.apis import APIHandlers as API

#create 2: one for openai, one for every other model
print("Welcome to MultiChat!")
print("What Provider would you like to use: openai, openrouter")
provider = input()
if provider.lower() == "openai":
    print("Here are the Large Language Models we have avaliable: 1 - o3-mini, 2 - o1-mini, 3 - o1, 4 - gpt-4o, 5 - gpt-4.5 preview, 6 - chatgpt-4o, 7 - gpt-4o mini")
    print("Which Large Language Model would you like to interact with?")
    userinput = input()
    text = userinput
    lower_text = text.lower()
    API.RunChat(lower_text, provider)









