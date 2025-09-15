'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto) # 1 2 [3, 4]

def soma(x, y):
    return x + y

print(1, 2, 3, 4, 5) # 1 2 3 4 5

soma(x, y) # Não aparece nada na tela

print(soma(x, y)) # 3

def sub(*args):
    print(args)

sub(1, 2, 3, 4, 5, 6, 7) # (1, 2, 3, 4, 5, 6, 7) -> uma tupla

# Brincando um pouco:

def lucas(*args):
    total = 0
    for x in args:
        print(x)
        total += x
    return total

resultado = lucas(10, 20, 30)
print('Total =', resultado)

"""
10
20
30
Total = 60
"""

# ou

print(sum((10, 20, 30))) # A função sum() funciona apenas com iterável (lista, tupla, etc)


# Com desempacotamento de valores
def mult(*args): # *args empacota em uma tupla
    total = 1
    for numero in args:
        print(numero, end=' ') # 1 2 3 4 5 6 
        total *= numero
    
    print('\n')
    return total

numeros = (1, 2, 3, 4, 5, 6)
result = mult(*numeros) # Desempacotamento da tupla numeros

print(result) # 720
