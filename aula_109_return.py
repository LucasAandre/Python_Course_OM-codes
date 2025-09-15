'''
Retorno de valores das funções (return)
'''

var = print('Lucas') # Lucas
print(var) # None

'''
Isso ocorre, pois print() é uma função com o intuito de imprimir
valores na tela. Ou seja, print() não tem nenhum valor, apenas
exibe valores.
'''

"""
def soma(x, y):
    print(x + y)

soma1 = soma(2, 2) # 4
soma2 = soma(3, 3) # 6
soma3 = soma1 + soma2
print(soma3) # Erro, pois soma1 e soma2 NÃO possuem valores!
"""

# Solução:

def subtracao(x, y):
    return x - y # Eu retorno um valor e não apenas o imprimo

sub1 = subtracao(4, 2) # 2
sub2 = subtracao(15, 3) # 12
sub3 = sub1 - sub2
print(sub3) # -10

'''
Eu não consigo colocar um print() após um return, dentro
de uma função.
'''

# A soma para quando um return é executado!
