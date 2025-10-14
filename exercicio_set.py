"""
Exercício

Crie uma função que encontre o primeiro valor duplicado, considerando o segundo
número como a duplicação. Retorne a duplicação considerada.

Requisitos:
A ordem do número duplicado é considerada a partir da segunda ocorrência do número,
ou seja, o número duplicado em si.

Exemplo:
    [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicado (retorne 3)
    [1, 2, 3, 4, 5, 6] -> não tem itens duplicados (retorne -1)
"""

# Não entendi muito bem, mas vamos lá...

s1 = set()
s2 = set()

def validacao():
    s3 = s1 & s2
    return s3

for i in range(1, 4):
    n = int(input(f'Digite o {i}º número inteiro: '))
    s1.add(n)

for i in range(4, 7):
    n = int(input(f'Digite o {i}º número inteiro: '))
    s2.add(n)

print('\nConjunto 1: ',s1)
print('\nConjunto 2: ',s2)

print(f'\nHá {len(validacao())} número(s) que se repete(m): {validacao()}')
