# Project Name
___
## About this Project
This project allows the user to access multiple large AI models through our website to use for necessary tasks.
___
## How to get started
### 1. Prerequisites

### 2. Download or Clone the Project

### 3. Open the Project Folder

### 4. Install Python Packages

### 5. Run the Project

## What Each File Does

### 1. main.py
       - The "main method" method of the program
       - The UI of the website
       - User will interact with the website through this code
### 2. JsonHandler.py
       - Printing the different AI models into model.json
       - Dumps the information from JsonHandler.py to model.josn
       - Allows us to access the information in model.json

### 3. model.json
       - Holds the information from JsonHandler.py

### APIHandlers.py
       - Goes into the backend and takes user saves files and makes them accessible to the developer
       - Takes the information (name, instructions, tools, model) and sends it to model's API to be accessed
       - Creates a chatroom (thread) with the selected AI
       - Creates a message that tells the AI that a user is accessing a thread and sending a message
       - Creates a run, which informs the I that there is a message and that it needs to respond
       - Assigns a unique ID to the thread and the AI assistant
       - Takes the responce from the AI and allows the program to grab it and print it for the user

### UserSaves.py
       - Creates a new chat or accesses a saved one

## How to Contribute
1. Fork this repository
2. Create a branch for your changes
3. Make your changes and test them
4. Submit a pull request so I can review your changes

## Known Issues
*enter issues here*