# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets
# difference - (elementos apenas no set da esquerda)
# symetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5,6,7,8,9,10}
print(s1)

for v in s1:
    print(v)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2
s3 = s1 - s2
s3 = s1 & s2
s3 = s1 | s2
print(s3)

