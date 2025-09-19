'''
Dicionários em Python (tipo dict)

Dicionários são estruturas de dados do tipo par de "chave" e "valor
Chaves podem ser consideradas como o "índice" que vimos na lista
e podem ser de tipos imutáveis, como: str, int, bool, float, tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.

Imutáveis: str, int, float, bool, tuple

Mutáveis: dict, list

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'André',
    'idade' : 26,
    'altura' : 1.69,
    'endereços' : [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 777},
    ],
}

print(pessoa, type(pessoa))
'''

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'André',
    'idade' : 26,
    'altura' : 1.69,
    'endereços' : [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 777},
    ],
}

print(pessoa['sobrenome']) # André
print(pessoa['endereços']) # [{'rua': 'tal tal', 'número': 123}, {'rua': 'outra rua', 'número': 777}]
print(pessoa['endereços'][0]['rua']) # tal tal

for chave in pessoa:
    print(chave, pessoa[chave])

"""
nome Lucas
sobrenome André
idade 26
altura 1.69
endereços [{'rua': 'tal tal', 'número': 123}, {'rua': 'outra rua', 'número': 777}]
"""
