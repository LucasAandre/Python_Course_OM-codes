'''
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis.
'''

# Forma de criar uma lista:
lista = []

for numero in range(10):
    lista.append(numero)

print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

# Criando com List Comprehension:
lista2 = [numero for numero in range(10)] # Inclua o número para cada número em um range de 0 a 10
print(lista2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista3 = [
    n * 2
    for n in range(10)
] # O dobro de cada número entre 0 e 10
print(lista3) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
