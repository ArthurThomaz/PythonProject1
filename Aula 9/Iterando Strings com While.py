
# While é utilizado para iterar sobre coisas que não sabemos o fim.

string = 'o rato roeu a roupa do rei de roma.'
string_lenght = len(string)

print(string.count('o')) # Vai contar quantas vezes ocorreu a ação. No caso quantas vezes aparece o O na string.

c = 0

new_string = ''

while c < string_lenght:
    if string[c] == 'r':
        new_string = new_string + string[c].upper()
    else:
        new_string += string[c]
    c += 1

print(new_string) # Print fora do laço While. Só ve o resultado.