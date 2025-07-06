'''
Formatando valores com modificadores: 

:s - Texto ( strings )
:d - Inteiro ( int )
:f - Números de ponto flutuante ( float )
:.(NÚMERO)f - Quantidade de casas decimais ( float )  # Exemplo: :.6f  ( 6 casas decimais )
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f) # 

< - Esquerda
> - Direita
^ - Centro
'''''

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

# print(divisao)

# print('{:.2f}'.format(divisao))

# print(f'{divisao:.2f}')


nome = "Arthur Thomaz"
nome_formatado = '{}'.format(nome)
nome_formatado = '{n}'.format(n=nome)

print( len(nome) )  #  "len" = Conta a quantidade de caracteres na string.

print(nome_formatado)

# Índices
nome_formatado = '{1}'.format(nome, sobrenome, qualquer, texto)
#                                    0        1         2        3
