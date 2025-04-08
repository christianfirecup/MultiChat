# Project Name
___
## About this Project
This project allows the user to access multiple large AI models through our website to use for necessary tasks.
___
## How to get started
### 1. Prerequisites
       Before you begin, make sure you have the following installed:
       - Python 3: You can dowload it from [python.org](https://www.python.org/downloads/).
       - Fit: (Optional) Needed if you want to clone the repository from GitHub. Download it from [git-scm.com](https://git-scm.com/).
       - OpenAI API Key: This project uses OpenAI services. You will need your API key saved in an environmental file.
       - Optional: Virtual Environment Tool: (Recommended) It's a good practice to run projects in an isolated environment.
### 2. Download or Clone the Project
        Option 1 - Clone the Repository (Recommended):
            1. Open your terminal (Comand Prompt, PowerShell, or Terminal on macOS/Linux).
            2. Run the following command (replace '<your-repo-url>' with your repository's URL):
        Option 2 - Download as ZIP:
            1. Downlaod the repository ZIP file form GitHub.
            2. Extract the ZIP file to your desired location. 

### 3. Open the Project Folder
    If you want to use a virtual environment, navigate to the project folder and run:
        # Create a virtual environment (named 'venv')
        python -m venv venv

        # Activate it:
        # On Windows:
        venv\Scripts\activate
        # On macOS/Linus:
        source venv/bin/activate
### 4. Install Python Packages
    Intall the required packages by running:
        pip install openain python-dotenv requrests
    
    If you have a requirements.txt file, you can install everything with:
        pip install -r requirements.txt

### 5. Set Up Environment Variables
    Create a file named .env in the root of your project and add your OpenAI API key:
        OAI=your_openai_api_key_here

### 6. Run the Project
    The main file contains the entry point (if_name_=="_main_":) and will launch the application. In your terminal, navigate to the directory containing the mian file. For example, if your main file is APIHandlers.py in the root (or inside a folder, e.g., src/apis/), run:
        python APIHanders.py
    Or, if it's in a different folder, adjust the path accordingly:
        python src/apis/APIHandlers.py

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