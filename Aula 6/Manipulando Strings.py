"""
* String Indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções Built in len, abs, type, print, etc.
"""""
# Sempre utilizar '[]' colchetes para indicar o índice.
# A contagem sempre começa no 0.
# O primeiro índice sempre é 0 e o último sempre o -1.

#Positivos   [01234567]
texto      = 'python02'
#Negativos  -[87654321]

# Apenas o índice
nova_string = texto[4]

#Fatiar
nova_string = texto[2:6]  # O índice final colocado não é incluído no que sai, porém o incial SEMPRE é incluído.
print(nova_string)  # Exemplo: "thon" = "2345"

nova_string = texto[:3] # Quando não tem índice inicial, ele pega do 0.
print(nova_string) # Exemplo: "pyt" = "012"

nova_string = texto[4:] # Quando não tem índice final ele pega até o último índice.
print(nova_string) # Exemplo: "on02" = "4567"
