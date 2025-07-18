secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print ('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh, isso não vale. Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Você acertou a letra {letra}.')
    else:
        print(f'Você errou, tente novamente.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você ganhou, a palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()