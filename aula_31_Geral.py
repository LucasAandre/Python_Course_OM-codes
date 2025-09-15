"""
Flag (bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
"""

v1 = 'a'
print(id(v1)) # Mostra a identidade (ID) da variável

# condicao = false

'''
if condicao:
    print('Faça algo')

else:
    print('Não faça algo')
'''

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')

else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) # Usado para validar se o interpretador passou pelo if. Se a variável continua como None, aparecerá True