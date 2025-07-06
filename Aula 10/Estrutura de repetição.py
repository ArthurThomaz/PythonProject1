'''
for in
iterando strings com for
função range(start=0, stop, step=1)
'''''

text = 'Python'
new_text = ''

for letter in text:

    if letter == 't':
        new_text += letter.upper()
        continue # Pula para próxima interação de repetilçao.

    elif letter == 'h':
        new_text += letter.upper()
        break # Para de executar.

    else:
        new_text += letter

print(new_text)