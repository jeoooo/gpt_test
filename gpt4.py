import g4f
import os
from dotenv import load_dotenv

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking

print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

chat_hist = []

# Automatic selection of provider
while True:
    msg = input('\nEnter message: ')

    # Append user message to chat history
    chat_hist.append({"role": "user", "content": msg})

    # Streamed completion
    response = g4f.ChatCompletion.create(
        auth=os.getenv('API_KEY'),
        model=g4f.models.gpt_4,
        messages=chat_hist,  # Pass the entire chat history
        stream=True,
    )

    for message in response:
        print(message, flush=True, end='')




# normal response
# response = g4f.ChatCompletion.create(
#     model=g4f.models.gpt_4,
#     messages=[{"role": "user", "content": "Hello"}],
# )  # alternative model setting

# print(response)