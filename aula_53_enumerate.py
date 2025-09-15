'''
ENUMERATE - Enumera iteráveis (índices)
'''

lista = ['Lucas', 'João', 'Rafaela', 'João']

for item in enumerate(lista):
    print(item)
    '''
    (0, 'Lucas')
    (1, 'João')
    (2, 'Rafaela')
    (3, 'João')
    '''
    # O enumerate cria uma tupla com índice e valor (i, v)

# ou

for item, nome in enumerate(lista, start=1):
    print(item, nome)
    '''
    1 Lucas
    2 João
    3 Rafaela
    4 João
    '''
    # Nesse caso, eu desempacotei as tuplas geradas. Mas existe outra forma (burra):

for i in enumerate(lista, start=1):
    a, b = i
    print(a, b)
    '''
    1 Lucas
    2 João
    3 Rafaela
    4 João
    '''