from src.apis import APIHandlers as API

print("Welcome to MultiChat!")
print("What Provider would you like to use: openai, openrouter")
provider = input()
if provider.lower() == "openai":
    print("Here are the Large Language Models we have avaliable: o3-mini, o1-mini, o1, gpt-4o, gpt-4.5 preview, chatgpt-4o, gpt-4o mini")
    print("Which Large Language Model would you like to interact with?")
    userinput = input()
    text = userinput
    lower_text = text.lower()
    API.RunChat(lower_text, provider)









