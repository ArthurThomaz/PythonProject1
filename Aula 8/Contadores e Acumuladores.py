'''
while/else
contadores
acumuladores
'''''

# While é utilizado para iterar sobre coisas que não sabemos o fim.

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else: # O Else só acontecerá se o While alcançar seu objetivo, que neste caso é o contador ser maior que 10.
    print('Finished.')


while contador <= 10:
    print(contador, acumulador)
    if contador > 5:
        break  # Se tiver um break no meio do laço, Else não será executado. Pois While ainda não se tornou False.
    acumulador = acumulador + contador
    contador += 1
else: print('Finished.').
