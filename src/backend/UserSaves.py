
import json
def load_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list.
        return []

# Helper function to save JSON data to a file.
def save_json_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def CreateUser():
    #user question
    print("MultiChat: Welcome to MC(MultiChat) please enter a name for you chat to save your data ")
    NTC = input("Name?: ")
    filename = 'data.json'
    #load json file
    data = load_json_file(filename)
    target_name = NTC
    found = False
    for entry in data:
        if entry.get('name') == target_name:
            print(f"Found {target_name} with id: {entry.get('id')}")
            found = True
            return entry.get('id')  # Changed from returning a set to returning the value directly
    if not found:
        # Local import to break the circular dependency
        from src.apis import APIHandlers as API
        thread = API.Create_Thread()
        new_id = thread.id
        new_entry = {'name': NTC, 'id': new_id}
        data.append(new_entry)
        save_json_file(filename, data)
        print(f"Added new entry: {new_entry}")
        return new_id

