import g4f


g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking

print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

with open('prompts/uwu_prompt.txt', 'r', encoding='UTF-8') as file:
    prompt_text = file.read()

    print(prompt_text)



chat_hist = [{"role": "system", "content": prompt_text}]

print(chat_hist)