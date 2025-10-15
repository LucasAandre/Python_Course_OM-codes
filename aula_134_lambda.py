# Introdução à Função Lambda + list.sort e sorted

'''
Função lambda em Python
A função lambda é uma função como qualquer outra em Python.
Porém, são funções anônimas que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma única expressão.

lista = [
    {'nome': 'Lucas', 'sobrenome': 'André'},
    {'nome': 'Pamela', 'sobrenone': 'Liberato'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Rodrygo', 'sobrenome': 'Goes'},
    {'nome': 'Neymar', 'sobrenome': 'Jr'},
]
'''

lista = [1, 5, 47, 6, 8, 21, 11]
lista.sort() # Ordena a lista
# sorted(lista) -> cria uma nova lista ordenada
# lista.sort(reverse=True) -> inverte a ordem da lista ordenada

print(lista) # [1, 5, 6, 8, 11, 21, 47]


lista2 = [
    {'nome': 'Lucas', 'sobrenome': 'André'},
    {'nome': 'Pamela', 'sobrenome': 'Liberato'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Rodrygo', 'sobrenome': 'Goes'},
    {'nome': 'Neymar', 'sobrenome': 'Jr'},
]

# Como faço para ordenar um dicionário?

def ordena(item):
    return item['nome'] # Ordena a lista pelo nome

lista2.sort(key=ordena) # A chave para ordenação é a função ordena

for item in lista2:
    print(item)
"""
{'nome': 'Daniel', 'sobrenome': 'Silva'}
{'nome': 'Lucas', 'sobrenome': 'André'}
{'nome': 'Neymar', 'sobrenome': 'Jr'}
{'nome': 'Pamela', 'sobrenone': 'Liberato'}
{'nome': 'Rodrygo', 'sobrenome': 'Goes'}
"""

print()

# Solução com função lambda:
lista2.sort(key=lambda item: item['sobrenome']) # Ordena a lista pelo sobrenome e não preciso declarar a função

for item in lista2:
    print(item)

"""
{'nome': 'Lucas', 'sobrenome': 'André'}
{'nome': 'Rodrygo', 'sobrenome': 'Goes'}
{'nome': 'Neymar', 'sobrenome': 'Jr'}
{'nome': 'Pamela', 'sobrenome': 'Liberato'}
{'nome': 'Daniel', 'sobrenome': 'Silva'}
"""

# Criando cópias, ao invés de editar a lista2:

print()

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista2, key=lambda item: item['nome'])
l2 = sorted(lista2, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
