while True:
    print()
    num_1 = input('Insira um numero: ')
    num_2 = input('Insira outro numero: ')
    operador = input('Insira operador: ')
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue
        num_1 = int(num_1)
        num_2 = int(num_2)
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador invalido')