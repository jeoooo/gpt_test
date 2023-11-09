import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider
while (True):

    msg = input('\nEnter message: ')

    # streamed completion
    response = g4f.ChatCompletion.create(
        provider=g4f.Provider.GeekGpt,
        model='gpt-4',
        messages=[
            {"role": "system", "content": "answer each question in tagalog."},
            {"role": "user", "content": msg}],
        stream=True,
    )
    for message in response:
        print(message, flush=false, end='')




# normal response
# response = g4f.ChatCompletion.create(
#     model=g4f.models.gpt_4,
#     messages=[{"role": "user", "content": "Hello"}],
# )  # alternative model setting

# print(response)