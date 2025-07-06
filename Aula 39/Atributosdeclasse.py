class A:
    x = 123
    def __init__(self):
        pass
a1 = A()
a2 = A()
A.x = 'Jabuti'
print(a1.x)
print(a2.x)
print(A.x)
