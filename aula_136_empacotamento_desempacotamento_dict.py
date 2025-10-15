# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b) # 2, 1

pessoa = {'nome': 'Nelvis', 'sobrenome': 'Silva'}
a, b = pessoa
print(a, b) # nome sobrenome

a, b = pessoa.values()
print(a, b) # Nelvis Silva

a, b = pessoa.items()
print(a, b) # ('nome', 'Nelvis') ('sobrenome', 'Silva')

(a1, a2), b = pessoa.items()
print(a2, b) # Nelvis ('sobrenome', 'Silva')

for chave, valor in pessoa.items():
    print(chave, valor)
"""
nome Nelvis
sobrenome Silva
"""

# Desempacotamento:
dados_pessoa = {
    'idade': 16,
    'altura': 1.69,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa) # {'nome': 'Nelvis', 'sobrenome': 'Silva', 'idade': 16, 'altura': 1.69}


# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

# Empacotando os argumentos no args e kwargs:
def argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

argumentos_nomeados('Pamela', 10, nome='Lucas', qualquer=11)
"""
Não nomeados: ('Pamela', 10)
nome Lucas
qualquer 11
"""

# Desempacotando:
argumentos_nomeados(**pessoa_completa)
"""
Não nomeados: ()
nome Nelvis
sobrenome Silva
idade 16
altura 1.69
"""
