# Manipulando chaves e valores em dicionários

pessoa = {}

# Criação de chave
pessoa['nome'] = 'Nelvis'

print(pessoa) # {'nome': 'Nelvis'}


# Manipulação de chave
chave = 'idade' # Uma variável -> chave dinâmica (posso alterar, sem problemas)

pessoa[chave] = 26 # -> chave dinâmica (posso alterar, sem problemas)

print(pessoa) # {'nome': 'Nelvis', 'idade': 26}


# Apagando uma chave:
del pessoa['idade']

print(pessoa) # {'nome': 'Nelvis'}


# Validando se uma chave existe:
if pessoa.get('sobrenome') is not None:
    print('Chave existe!')

else:
    print('Chave não existe')
