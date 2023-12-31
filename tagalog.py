import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

with open('prompts/tagalog_prompt.txt', 'r', encoding='UTF-8') as file:
    prompt_text = file.read()


chat_hist = [{"role": "system", "content": prompt_text}]

# Automatic selection of provider
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