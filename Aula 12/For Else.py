'''
For / Else
'''''

Variavell = ['Luiz Otavio', 'Joaozinho', 'Maria']

for valor in Variavell:
    print(valor)
    break
    print(valor)

for valor in Variavell:
    if valor.startswith('L'):
        print('Começa com L.')
    else:
        print('Não começa com L')

comeca_com_j = False

for valor in Variavell:
    if valor.startswith('L'):
        comca_com_j = True

if comca_com_j:
    print('Existe uma palavra que começa com L.')
else:
    print('Não tem palavra que começa com L')

