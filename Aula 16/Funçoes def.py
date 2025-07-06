'''
Funções - def
'''''

def funcao():
    print('Hello World!')
funcao()
funcao()
funcao()
funcao()
funcao()

def saudacao(msg, nome):
    print(msg, nome)
saudacao('Hello', 'world!')
saudacao('Ola', 'Arthur')
saudacao('Ola', 'Mundo.')
saudacao('Ola', 'Joaozinho e Maria')

def saudation(msg='Hello', nome='world'):
    nome = nome.replace('o', 'K')
    msg = msg.replace('o', 'K')
    print(msg, nome)
saudation('Ola', 'Mundo')
saudation('Ola', 'Joaozinho e Maria')

def funcao(var):
    return var
    print('Isso nao sera executado.')

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')


def divisao(n_1, n_2):
    return n_1 / n_2

divide = divisao(8, 4)
print(divide)

