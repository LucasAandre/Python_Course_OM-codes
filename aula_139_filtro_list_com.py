import pprint # Um módulo do Python

def p(v):
    # Um print mais bonito e com personalizações:
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.50}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# Um filtro é um if que vem depois do for
# Na condição que antece o for, SEMPRE terei um if e um else
# No filtro (condição que é posterior ao for), eu terei apenas um if

p(novos_produtos)
"""
[{'nome': 'p1', 'preco': 20},
 {'nome': 'p2', 'preco': 10},
 {'nome': 'p3', 'preco': 45.0}]
"""

lista = [n for n in range(10)]
#lista = list(n for n in range(10))

print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# FILTRO:

# Inclua um número se ele for menor do que 5:
lista2 = [n for n in range(10) if n < 5]
print(lista2) # [0, 1, 2, 3, 4]

# MAPEAMENTO:
lista3 = [n if n < 5 else 'L' for n in range(10)]
print(lista3) # [0, 1, 2, 3, 4, 'L', 'L', 'L', 'L', 'L']


# Junção de MAPEAMENTO e FILTRO:

'''
Quero incluir na lista apenas produtos que custem mais que 10 e, para produtos que
custem mais que 20, quero acrescentar um aumento de 5%:
'''

novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos2)
'''
[{'nome': 'p1', 'preco': 20},
 {'nome': 'p3', 'preco': 31.5}]
'''
