def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print(error)
        raise
try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print('Erro')

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 cannot be zero.')
    return n1/n2
try:
    print(divide(2, 0))
except ValueError as error:
    print('You are trying to divide by zero.')
    print(error)
