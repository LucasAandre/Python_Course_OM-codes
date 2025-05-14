'''
LISTAS EM PYTHON

Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete -> CRUD
Criar, Ler, Atualizar, Apagar = lista[i]
'''

#          01234
#         -54321
strings = 'ABCDE' # 5 caracteres (len)

# Declaração de uma lista vazia
lista1 = []
lista2 = list()

# Lista com valores
numeros = [1, 2, 3, 4, 5]
nomes = ['Ana', 'Lucas', 'Pamela']
misturado = [10, 'Liberato', 22, True, 3.14, []]
print(misturado[1], type(misturado[1])) # Liberato <class 'str'>

# Lista com range()
sorteio = list(range(5)) # [0, 1, 2, 3, 4]
sorteio2 = list(range(2, 10, 2)) # [2, 4, 6, 8]

# Compreensão de lista (list comprehension)
quadrados = [x**2 for x in range(10)] # [0, 1, 4, ..., 81] -> 1², 2², 3², ..., 9²
pares = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, 6, ..., 18]

# Conversão de outros tipos para lista
texto = 'Neymar'
change = list(texto) # ['N', 'e', 'y', 'm', 'a', 'r']

tupla = (1, 2, 3)
change2 = list(tupla) # [1, 2, 3]

# Mudança de valores em uma lista

#         - 5       4      3       2         1
#           0       1      2       3         4
lista3 = ['Adão', 'Eva', 'Noé', 'Moisés', 'Josué']
lista3[2] = 'Jó'
print(lista3) # ['Adão', 'Eva', 'Jó', 'Moisés', 'Josué']

# Uso de valores de uma lista
inteiros = [1, 2, 3, 4, 5]
inteiro = inteiros[4] # Criei uma variável e dei a ela o valor do índice 4 da minha lista

# Apagando valores em uma lista
lista4 = [23, 55, 303, 48, -1]
del lista4[3]
print(lista4) # [23, 55, 303, -1]

# Adicionando valores ao final de uma lista
lista5 = [23, 55, 303, 48, -1]
lista5.append(115) # Adiciona ao final da lista o valor digitado
print(lista5) # [23, 55, 303, 48, -1, 115]

# Removendo valores em uma lista (similar ao apagar)
lista6 = [23, 55, 303, 48, -1]
lista6.pop() # Remove o último valor da lista
print(lista6) # [23, 55, 303, 48]
ultimo = lista6.pop()
print('Último valor removido:', ultimo) # Último valor removido: 48

# Removendo valores internos da uma lista (similar ao apagar)
lista7 = [23, 55, 303, 48, -1]
lista7.pop(2) # Coloco o índice que quero remover
print(lista7) # [23, 55, 48, -1]

# Limpando uma lista
lista8 = [23, 55, 303, 48, -1]
lista8.clear()
print(lista8) # []

# Inserindo valores em um determinado índice de uma lista
lista9 = [23, 55, 303, 48, -1]
lista9.insert(1, 11) # Adicionando o número 11 no índice 1
print(lista9) # [23, 11, 55, 303, 48, -1]
'''
Caso eu adicione um índice maior do que, de fato, existe na lista, o valor será adicionado
ao final da lista, como se fosse um append()
'''

# Concatenando listas
lista_a = [1, 2, 3]
lista_b = ['Um', 'Dois', 'Três']
lista_c = lista_a + lista_b
print(lista_c) # [1, 2, 3, 'Um', 'Dois', 'Três']

# Estendendo listas
lista_d = [1, 2, 3]
lista_e = ['Um', 'Dois', 'Três']
lista_f = lista_d.extend(lista_e)
print(lista_f) # None -> executou a ação, mas não retornou nenhum valor. Ou seja, mexeu diretamente no valor (lista_d)
print(lista_d) # [1, 2, 3, 'Um', 'Dois', 'Três']

# Adicionando valores nas listas com dados digitados pelo usuário
valores = []

quantidade = int(input('Quantos valores deseja adicionar à lista? '))

for i in range(quantidade):
    valor = input(f'Digite o {i+1}º valor: ')
    valores.append(valor)

print('Lista final:', valores)

# ou

valores2 = []

while True:
    entrada = input('Digite um valor (ou "sair" para encerrar): ')
    if entrada.lower() == 'sair':
        break
    valores2.append(entrada)

print('Lista final:', valores2)

# Escolher um valor aleatório da lista
import random

lista = ['maçã', 'banana', 'uva', 'laranja']
sorteado = random.choice(lista)

print('Valor sorteado:', sorteado)

# Sortear vários valores diferentes
import random

lista = [1, 2, 3, 4, 5, 6]
sorteados = random.sample(lista, 3)  # sorteia 3 valores diferentes

print('Valores sorteados:', sorteados)

# Embaralhar toda a lista
import random

lista = ["A", "B", "C", "D"]
random.shuffle(lista)

print("Lista embaralhada:", lista)

# Sortear com repetição
import random

lista = [10, 20, 30]
sorteios = random.choices(lista, k=5)  # sorteia 5 valores com possibilidade de repetição

print('Sorteios:', sorteios)

# Gerar números inteiros aleatórios
import random

lista = []

for _ in range(10):  # 10 números
    numero = random.randint(1, 100)  # entre 1 e 100
    lista.append(numero)

print('Números aleatórios:', lista)

# ou

import random

lista = [random.randint(1, 100) for _ in range(10)]
print('Lista:', lista)

# Gerar números decimais aleatórios
import random

lista = [round(random.uniform(1, 10), 2) for _ in range(5)]
print('Números decimais:', lista)

# Operações matemáticas
'''
ADIÇÃO
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

soma = [lista1[0] + lista2[0], lista1[1] + lista2[1], lista1[2] + lista2[2]]
print(soma)  # [5, 7, 9]

# ou

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

soma = [a + b for a, b in zip(lista1, lista2)]
print(soma)  # [5, 7, 9]

# ou

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

soma_total = sum(lista1) + sum(lista2)
print(soma_total)  # 21

'''
SUBTRAÇÃO
'''
resultado = [a - b for a, b in zip(lista1, lista2)]
print(resultado)  # [-3, -3, -3]

'''
MULTIPLICAÇÃO
'''
resultado = [a * b for a, b in zip(lista1, lista2)]
print(resultado)  # [4, 10, 18]

'''
DIVISÃO
'''
resultado = [a / b for a, b in zip(lista1, lista2)]
print(resultado)  # [0.25, 0.4, 0.5]
