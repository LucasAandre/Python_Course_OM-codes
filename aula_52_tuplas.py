'''
Tuplas em Python
'''

# Tupla: uma Lista imutável
'''
Uma tupla é mais eficiente (rápida) do que uma lista. Por isso, se você não quiser
alterar algo na lista, faz mais sentido criar uma tupla.
'''

# Declarando uma tupla
nomes = ('Michael', 'Jim', 'Pam', 'Dwight')

# ou

novos_nomes = 'Michael', 'Jim', 'Pam', 'Dwight'

print(nomes, type(nomes)) # ('Michael', 'Jim', 'Pam', 'Dwight') <class 'tuple'>
print(novos_nomes, type(novos_nomes)) # ('Michael', 'Jim', 'Pam', 'Dwight') <class 'tuple'>

print(nomes[2]) # Pam

# Convertendo uma lista para um tupla
dados = ['Lucas', 26, 'Pamela', 22]
dados = tuple(dados)
print(dados) # ('Lucas', 26, 'Pamela', 22)

# Convertendo uma tupla em uma lista
a = (15, 29, 45, False)
a = list(a)
print(a) # [15, 29, 45, False]
