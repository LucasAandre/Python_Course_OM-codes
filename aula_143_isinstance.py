# isinstance - para saber se objeto é de determinado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Lucas'}]

for item in lista:
    print(item, isinstance(item, set)) # Checando se o item é um set

    '''
    a False
    1 False
    1.1 False
    True False
    [0, 1, 2] False
    (1, 2) False
    {0, 1} True
    {'nome': 'Lucas'} False
    '''

print()

for item in lista:
    if isinstance(item, set):
        item.add(11)
        print(f'{item} é um set? R: {isinstance(item, set)}')
        # {0, 1, 11} é um set? R: True
    
    elif isinstance(item, str):
        print(item.upper())
    
    elif isinstance(item, (int, float)): # Se for int ou float
        print(f'O dobro de {item} é {item * 2}')
    
    else:
        print(item)

'''
A
O dobro de 1 é 2
O dobro de 1.1 é 2.2
O dobro de True é 2
[0, 1, 2]
(1, 2)
{0, 1, 11} é um set? R: True
{'nome': 'Lucas'}
'''     
