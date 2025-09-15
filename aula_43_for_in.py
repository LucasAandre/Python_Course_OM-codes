'''
Introdução ao for / in - estrutura de repetição para coisas finitas
'''

texto = 'Adulto Ney'
novo_texto = ''

for letra in texto:
    print(letra) # Imprime uma letra por linha
    novo_texto += f'{letra}*'

print(novo_texto) # Imprime A*d*u*l*t*o* *N*e*y*

'''
USO DE RANGER

O range() é usado para gerar uma sequência de números. Ele é muito usado em laços for quando você quer repetir algo um número específico de vezes.

Sintaxe:
for i in range(início, fim, passo):
    código

Exemplos:
for i in range(5):
    print(i) # 0 1 2 3 4

for c in range(2, 6):
    print(c) # 2 3 4 5

for l in range(10, 0, -2):
    print(l) # 10 8 6 4 2
'''

'''
USO DE ENUMERATE

O enumerate() é usado quando você precisa iterar sobre uma lista (ou outro iterável) e também quer saber o índice de cada item.

Sintaxe:
for índice, valor in enumerate(lista, início=0):
    código

Exemplos:
frutas = ['maçã', 'banana', 'laranja']

for i, fruta in enumerate(frutas):
    print(f'{i}: {fruta}') # 0: maçã 1: banana 2: laranja

for i, fruta in enumerate(frutas, start=1):
    print(f'{i}: {fruta}') # 1: maçã 2: banana 3: laranja
'''