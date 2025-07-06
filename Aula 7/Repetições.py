'''
while em Python
utilização para realizar ações enquanto 
uma condição for verdadeira

Requisitos: Entender condições e operadores.
'''''

# While é utilizado para iterar sobre coisas que não sabemos o fim.

x = 0

while x < 10:
    if x == 3:
        x = x +1 # Forma abreviada: x += 1
        continue

    print(x)
    x = x + 1 # Forma abreviada da expressão: x += 1

while x < 10:
    y = 0

    while y < 4:
        print(f'{x},{y}')
        y += 1

    x += 1

while True: # Loop infinito
    nome = input('Digite seu nome: ')
    print(f"Hi! {nome}. Welcome.")

print("Esta ação nunca será realizada.")
