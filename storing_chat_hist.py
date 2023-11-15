import g4f
import os

g4f.debug.logging = True  # enable logging
g4f.check_version = False  # Disable automatic version checking

print(g4f.version)  # check version
print(g4f.Provider.Ails.params)  # supported args

with open('prompts/uwu_prompt.txt', 'r', encoding='UTF-8') as file:
    prompt_text = file.read()

    print(prompt_text)

chat_hist = [{"role": "system", "content": prompt_text}]

# Specify the path for the chat history file
chat_history_path = 'chat history/chat_history.txt'

# Ensure the directory exists
os.makedirs(os.path.dirname(chat_history_path), exist_ok=True)

# Open a file to store messages and chat history
with open(chat_history_path, 'a', encoding='UTF-8') as chat_file:
    # Automatic selection of provider
    while True:
        msg = input('\nEnter message: ')

        # Append user message to chat history
        chat_hist.append({"role": "user", "content": msg})

        # Streamed completion
        response = g4f.ChatCompletion.create(
            provider=g4f.Provider.GeekGpt,
            model=g4f.models.gpt_35_turbo_16k_0613,
            messages=chat_hist,  # Pass the entire chat history
            stream=True,
        )

        for message in response:
            # Print and write the message to the file
            print(message, flush=True, end='')
            chat_file.write(message)

        # Convert the entire chat history to a string and write to the file
        chat_history_str = '\n'.join([f"{item['role']}: {item['content']}" for item in chat_hist])
        chat_file.write(chat_history_str + '\n')
