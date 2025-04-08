# MultiChat

MultiChat is a Python-based multi-provider chatbot that supports OpenAI’s Assistants API (and is structured for future OpenRouter integration). It allows users to select from multiple LLMs, spin up assistants, save conversations, and interact via terminal.

## Setup

1. Clone the repository:

   git clone https://github.com/yourusername/MultiChat.git  
   cd MultiChat

2. Install required dependencies:

   pip install openai python-dotenv

3. Create a .env file in the root directory and add your OpenAI API key:

   OAI=your_openai_api_key_here

## How to Run

Run the main script:

   python src/application/main.py

You will be prompted to:
- Choose a provider (e.g., openai)
- Select a model (e.g., gpt-4o)
- Name your conversation
- Start chatting

## Features

- Supports OpenAI Assistants API
- Remembers and saves your threads and messages
- Uses openai.json to map assistant IDs to model names
- Prepares for future support of OpenRouter
- CLI-based interaction

## File Descriptions

| File             | Description                                      |
|------------------|--------------------------------------------------|
| main.py          | Entry point CLI for user interaction             |
| APIHandlers.py   | Assistant creation, thread/message/run logic     |
| UserSaves.py     | Handles saving/loading thread data and user prompts |
| openai.json      | Maps assistant IDs to model names                |
| data.json        | Stores per-user thread metadata                  |
| .env             | Your OpenAI API key (keep this private)          |

## Future Plans

- OpenRouter integration
- Assistant creation when missing from config
- GUI option
- Richer data storage (e.g., database)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
