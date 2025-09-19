'''
Méotodos úteis dos dicionários em Python

len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

usuario = {
    'nome': 'Neymar Jr',
    'sobrenome': 'Silva',
    'sobrenome': 'Pereira',
    'sobrenome': 'Santos'
}

# len
print(usuario.__len__()) # 2
print(len(usuario)) # 2


# Se eu criar chaves iguais em um dicionário, apenas o último valor adicionado será considerado:
print(usuario) # {'nome': 'Neymar Jr', 'sobrenome': 'Santos'}


# keys
print(usuario.keys()) # dict_keys(['nome', 'sobrenome']) -> retorna as chaves

# values
print(usuario.values()) # dict_values(['Neymar Jr', 'Santos'])

# items
print(usuario.items()) # dict_items([('nome', 'Neymar Jr'), ('sobrenome', 'Santos')])


# Eu posso converter esses métodos em listas:
print(list(usuario.keys())) # ['nome', 'sobrenome']

print(list(usuario.values())) # ['Neymar Jr', 'Santos']

print(list(usuario.items())) # [('nome', 'Neymar Jr'), ('sobrenome', 'Santos')]


# setdefault
usuario.setdefault('idade', 33) # Se a chave já existir, não altera nada!
print(usuario['idade']) # 33
print(usuario) # {'nome': 'Neymar Jr', 'sobrenome': 'Santos', 'idade': 33}


d1 = {
    'c1': 1,
    'c2': 2
}

d2 = d1 # Aqui, eu não estou criando uma cópia. Estou dizendo que d2 apontará para d1
# Logo, se eu fizer uma alteração em d2, estarei alterando d1


# copy
d3 = d1.copy() # Faço uma cópia de tudo o que for imutável

d4 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d5 = d4.copy() # Nesse caso, não foi uma cópia, pois temos uma lista, que é MUTÁVEL
# Dessa forma, c1 e c2 são CÓPIAS, mas l1 aponta para d4

d5['c1'] = 16
d5['l1'][1] = 450


print(d4) # {'c1': 1, 'c2': 2, 'l1': [0, 450, 2]}
print(d5) # {'c1': 16, 'c2': 2, 'l1': [0, 450, 2]}

# Mas se eu fizer uma alteração geral:
d5['l1'] = 'Lucas'

print(d4) # {'c1': 1, 'c2': 2, 'l1': [0, 450, 2]}
print(d5) # {'c1': 16, 'c2': 2, 'l1': 'Lucas'}


# Quando eu quiser uma cópia profunda:
import copy

d6 = copy.deepcopy(d4)

print(d6) # {'c1': 1, 'c2': 2, 'l1': [0, 450, 2]}


# get
print(usuario.get('nome')) # Neymar Jr
print(usuario.get('Altura')) # None (a chave não existe)
print(usuario.get('altura', 'Chave não existe')) # Chave não existe


# pop
nome = usuario.pop('nome')
print(nome) # Neymar Jr
print(usuario) # {'sobrenome': 'Santos', 'idade': 33}
# Eu salvei o nome em uma var e excluí a chave 'nome'

usuario['nome'] = 'Neymar Jr'
print(usuario) # {'sobrenome': 'Santos', 'idade': 33, 'nome': 'Neymar Jr'}


# popitem
ultima_chave = usuario.popitem()
print(ultima_chave) # ('nome', 'Neymar Jr')
print(usuario) # {'sobrenome': 'Santos', 'idade': 33}
# Removi a última chave do meu dicionário

usuario['nome'] = 'Neymar Jr'
print(usuario) # {'sobrenome': 'Santos', 'idade': 33, 'nome': 'Neymar Jr'}


# update

#01
usuario.update({
    'nome': 'Lucas',
    'time': 'Santos'
})

print(usuario) # {'sobrenome': 'Santos', 'idade': 33, 'nome': 'Lucas', 'time': 'Santos'}
# Eu consigo modificar chaves e até mesmo adicionar novas

#02
usuario.update(nome='Nelvis', idade=26)
print(usuario) # {'sobrenome': 'Santos', 'idade': 26, 'nome': 'Nelvis', 'time': 'Santos'}

#03
tupla = (('nome', 'Neymar Jr'),)
usuario.update(tupla)
print(usuario) # {'sobrenome': 'Santos', 'idade': 26, 'nome': 'Neymar Jr', 'time': 'Santos'}

#04
lista = [['nome', 'Neymar Jr'], ['idade', 33]]
usuario.update(lista)
print(usuario) # {'sobrenome': 'Santos', 'idade': 33, 'nome': 'Neymar Jr', 'time': 'Santos'}
