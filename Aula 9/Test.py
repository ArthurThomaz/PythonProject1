while True:      # Para ser um loop, e verificar a frase sme parar. Precisa ser um input.
    string = input('Digite uma frase: ')
    string_lenght = len(string)

    c = 0

    contagem = 0
    letra = ''

    while c < string_lenght:
        conta = string.count(string[c])

        if contagem < conta and string[c].strip():
            letra = string[c]
            contagem = conta

        # print(string[c], conta)

        c += 1

    print(letra, contagem)
