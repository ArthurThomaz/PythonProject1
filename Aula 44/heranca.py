from classsses import *
'''
Associaçao - Usa / Agregaçao - Tem / Composiçao - É dono / Herança - É
'''''

c1 = Cliente('Arthur', 25)
c1.falar()
c1.comprar()
c1.estudar() # Estudar esta apenas para Aluno

a1 = Aluno('Julian', 59)
a1.falar()
a1.estudar()
a1.comprar() # Comprar esta apenas para Cliente

p1 = Pessoa('Ana', 40)
p1.falar()
p1.estudar() # Estudar nao esta para Pessoa
p1.comprar() # Comprar nao esta para Pessoa, apenas o Falar