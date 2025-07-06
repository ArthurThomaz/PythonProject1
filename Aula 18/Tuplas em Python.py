t1 = (1, 2, 3, 4, 5)
print(t1[4])

for v in t1:
    print(v)

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 99
t1 = tuple(t1)
print(t1)

# Tuples não podem ser alteradas.