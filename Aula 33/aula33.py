# https://docs.python.org/3/library/functions.html#open

file = open('abc.txt', 'w+')
file.write('line 1\n') # \n = Adiciona uma quebra de linha.
file.write('line 2\n')
file.write('line 3\n')
file.seek(0, 0) # Volta o cursor para as coordenadas dadas.
print('Reading lines.')
print(file.read())
file.seek(0, 0)
print(file.readline(), end='') # ( end='' ) = Retira a quebra de linha.
print(file.readline(), end='')
print(file.readline(), end='')
file.seek(0, 0)
for line in file.readlines():
    print(line, end='')
file.close()


# Forma não recomendada para se usar no Python
try:
    file = open('abc.txt', 'w+')
    file.write('Line')
    file.seek(0)
    print(file.read())
finally:
    file.close()

# Forma mais pratica, pois não precisa colocar para finalizar.
with open('abc.txt', 'w+') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    file.seek(0, 0)
    print(file.read())

# Com o 'a+', para adicionar coisas no arquivo, sem apagar.
with open('abc.txt', 'a+') as file:
    file.write('Another line\n')
    file.seek(0)
    print(file.read())

import os
os.remove('abc.txt')

import json
d1 = {
    'Person 1': {
        'name': 'Arthur',
        'age': 24,
    },
    'Person 2': {
        'name': 'Joao',
        'age': 30,
    }
}
d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)

