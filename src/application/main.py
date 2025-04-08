import json
import os

#create 2: one for openai, one for every other model
file_path = 'model.json'
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        json.dump([], f)

print("Welcome to MultiChat!")
print("Here are the Large Language Models we have avaliable: 1 - o3-mini, 2 - o1-mini, 3 - o1, 4 - dall.e, 5 - gpt-4o, 6 - gpt-4.5 preview, 7 - chatgpt-4o, 8 - gpt-4o mini")
print("Which Large Language Model would you like to interact with?")
userinput = input()
text = userinput
lower_text = text.lower()

print(f"Accessing {userinput} now")

with open(file_path, 'r') as f:
    data = json.load(f)

data.append({"model": userinput})
with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)






