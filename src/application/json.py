import json

data = {
    "1": "o3-mini",

    "2": "o1-mini",

    "3": "o1",

    "4": "dall.e 3",

    "5": "gpt-4o",

    "6": "gpt-4.5 preview",

    "7": "chatgpt-4o",
    
    "8": "gpt-4o mini",
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
