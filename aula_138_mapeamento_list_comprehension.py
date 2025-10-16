# Mapeamento de dados em lists comprehension

lista = [
    n * 2
    for n in range(10)
] # O dobro de cada número entre 0 e 10
print(lista) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

"""
Mapear nada mais é do que saber em qual posição os itens estão.
Ou seja, mesmo multiplicando por 2, o tamanho da lista continua o mesmo,
mesmo que eu não tivesse feito nada com o n.
"""


# Outro exemplo de mapeamento:
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [produto for produto in produtos]

print(novos_produtos) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 30}]
# Isso acima já é um mapeamento

# Desempacotando:
print(*novos_produtos, sep='\n')
'''
{'nome': 'p1', 'preco': 20}
{'nome': 'p2', 'preco': 10}
{'nome': 'p3', 'preco': 30}
'''

print()

produtos2 = [produto['nome'] for produto in produtos]

print(produtos2) # ['p1', 'p2', 'p3']

print(*produtos2, sep='\n')
'''
p1
p2
p3
'''

print()

# Criando uma nova lista com dicionários internos:
produtos3 = [
    {'número': produto['preco']}
    for produto in produtos
]

print(produtos3) # [{'número': 20}, {'número': 10}, {'número': 30}]

print()

produtos4 = [
    {**produto, 'preco': produto['preco']*1.05}
    for produto in produtos
] # Criação de uma nova lista com dicionários, com os mesmos nomes, mas com preços diferentes
# O **produto serve para desempacotar os dicionários. Dessa forma, estou alterando apenas os preços.
# Se eu não desempacotar os dicionários, não conseguirei alterar os preços.

print(*produtos4, sep='\n')
'''
{'nome': 'p1', 'preco': 21.0}
{'nome': 'p2', 'preco': 10.5}
{'nome': 'p3', 'preco': 31.5}
'''

print()

# Exemplo com condição:
produtos5 = [
    {**produto, 'preco': produto['preco']*1.80}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*produtos5, sep='\n')
'''
{'nome': 'p1', 'preco': 20}
{'nome': 'p2', 'preco': 10}
{'nome': 'p3', 'preco': 54.0}
'''
