# Dictionary Comprehension e Set Comprehension
produto = {'nome': 'Caneta Azul', 'preco': 2.5, 'categoria': 'Escritório',}

for chave, valor in produto.items():
    print(chave, valor)
'''
nome Caneta Azul
preco 2.5
categoria Escritório
'''

dc = {chave: valor for chave, valor in produto.items()}
print(dc) # {'nome': 'Caneta Azul', 'preco': 2.5, 'categoria': 'Escritório'}

# Mesma coisa de lista, mas com dicionários


# Set Comprehension:
s1 = {i for i in range(10)}
print(s1)


# Para tupla() não dá certo...
