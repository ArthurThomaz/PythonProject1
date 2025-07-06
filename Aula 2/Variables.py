'''
Variéveis são usadas para armazenar valores
e dar nome a um trecho da memória do computador
onde os valores estão armazenados.

Quando uma variável é criada, o Python já determina seu tipo
de acordo com seu valor. 
Isso se chama tipagem dinâmica,

Nomes de variáveis devem começar com uma letra
Nomes de variáveis podem conter números
Nome compostos podem ser separados por um _
Por conversão utilize apenas letras minúsculas
'''''

nome = 'Arthur' # string
idade = 25 # int
altura = 1.80 # float
peso = 75 # int
data_atual = '20/06/2025' # string

# Fórmula IMC (Índice de Massa Corporal) = peso dividido pelo quadrado da altura
indice_de_massa_corporal = peso / (altura**2)

print("A variável nome recebeu:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("data_atual:", data_atual)
print(nome, "tem", idade, "anos e seu IMC é", indice_de_massa_corporal)

#
# a função format é usada em strings para formatar o texto
# # de maneira que a leitura e a escrita fiquem mais fáceis
print("{} tem {} anos e seu IMC é {}." .format(nome, idade, indice_de_massa_corporal))

# outro exemplo
print(f"{nome} tem {idade} anos e seu IMC é de: {indice_de_massa_corporal}")
