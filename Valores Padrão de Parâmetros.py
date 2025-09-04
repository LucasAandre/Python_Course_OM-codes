"""
Valores padrão para um parâmetro
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão
será usado.

Refatorar: Editar o código.
"""

'''
Em Python, o valor 0 (zero) é considerado FALSE
Dessa forma, mesmo se um parâmetro for definido como zero,
o código entenderá que o parâmetro não tem valor!
Veja:
'''

def soma(x, y, z=0):
    if z: # Se z = True
        print(f'{x = } {y = } {z = }')
    
    else: # Se z = False
        print(f'{x = } {y = }')

soma(1, 5, 0) # x = 1 y = 5

'''
No exemplo acima, o usuário definiu o z = 0, mas o código entendeu 
que z não foi definido.
'''

# Solução
def xuxu(x, y, z=0):
    if z is not None:
        print(f'{x = } | {y = } | {z = }')
    
    else:
        print(f'{x = } | {y = }')

xuxu(89, 5, 0) # x = 89 | y = 5 | z = 0


def lucas(x, y, z = 'Carlos'):
    print(f'{x = } | {y = } | {z = }')

lucas('Caio', 0) # x = 'Caio' | y = 0 | z = 'Carlos'
lucas('Pamela', True, 'Neymar') # x = 'Pamela' | y = True | z = 'Neymar'
lucas(y = 14.77, z = 'Lucas', x = 0) # x = 0 | y = 14.77 | z = 'Lucas'
