import json

data = {
    "1": "o3-mini",

    "2": "o1-mini",

    "3": "o1",

    "4": "gpt-4o",

    "5": "gpt-4.5 preview",

    "6": "chatgpt-4o",
    
    "7": "gpt-4o mini",
}

with open("openai.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

with open("openai.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
    print("completed")
