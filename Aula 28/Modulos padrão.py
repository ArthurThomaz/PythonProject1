import sys
print(sys.platform) # Importando módulo inteiro

from sys import platform
print(platform)

from sys import platform as so
print(so)

from random import randint
for i in range(10):
    print(randint(1,10))

from random import *
for i in range(10):
    print(randint(0,10))
