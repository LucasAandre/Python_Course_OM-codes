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
