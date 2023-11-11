

"""
This script allows the user to interact with an AI chatbot using the g4f library. 
The chatbot uses the GeekGpt provider and the gpt_35_turbo_16k_0613 model to generate responses based on the user's input. 
The chat history is stored in the chat_hist list and is passed to the chatbot for context. 
The script also enables logging and disables automatic version checking.

"""
import g4f


g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking

print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

with open('prompts/binary_prompt.txt', 'r', encoding='UTF-8') as file:
    prompt_text = file.read()

    print(prompt_text)



chat_hist = [{"role": "system", "content": prompt_text}]

print(chat_hist)
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
        print(message, flush=True, end='')