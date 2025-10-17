lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y)) # Adicionando um tupla na lista

print(lista) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print()
# Solução com list comprehension:
lista = [
    (x, y) for x in range(3)
    for y in range(3)
]

print(lista) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print()

lista = [
    [x for y in range(3)]
    for x in range(3)
] # Uma list comprehension dentro de outra

print(lista) # [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

print()

lista = [
    [x for x in range(3)]
    for x in range(3)
] # Uma list comprehension dentro de outra

print(lista) # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

print()

lista = [
    [letra for letra in 'Lucas']
    for x in range(3)
]

print(lista) # [['L', 'u', 'c', 'a', 's'], ['L', 'u', 'c', 'a', 's'], ['L', 'u', 'c', 'a', 's']]
