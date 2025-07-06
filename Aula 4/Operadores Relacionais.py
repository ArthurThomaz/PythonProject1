''''
Operdores Relacionais 
==  >  >=  <  <=  !=
'''''

# 1 sinal de igual, você esta afirmando.
# 2 sinais de igual, você esta perguntando se algo é verdadeiro

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

idade = int(idade)

# Limite para pegar empréstimo.
# Para atribuir valor a algum objeto é preciso o uso de " = " ( igual )

idade_menor = 20 # Mínimo de idade
idade_maior = 30 # Máximo de idade

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} tem direito a pegar o empréstimo.")

else:
    print(f"{nome} não tem direito a pegar empréstimo.")
