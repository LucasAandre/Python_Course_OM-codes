# Exercícios sobre list comprehension

''''
1. Crie uma list comprehension que gere uma lista com todos os números pares de
0 a 20 (inclusive).

Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


2. A partir da lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9], crie uma nova lista
contendo os quadrados apenas dos números ímpares.

Saída: [1, 9, 25, 49, 81]


3. Dada a lista palavras = ["Python", "é", "uma", "linguagem", "poderosa", "e", "simples"],
crie uma list comprehension que contenha apenas as palavras com mais de 4 letras, todas em 
letras maiúsculas.

Saída: ["PYTHON", "LINGUAGEM", "PODEROSA", "SIMPLES"]

'''

# Exercício 1
pares = [n for n in range(22) if n % 2 == 0]

print(pares) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print()


# Exercício 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

quadrados = [(n**2) for n in numeros if n % 2 != 0]

print(quadrados) # [1, 9, 25, 49, 81]

print()


# Exercício 3
palavras = ['Python', 'é', 'uma', 'linguagem', 'poderosa', 'e', 'simples']

new_words = [
    palavra.upper() for palavra in palavras
    if len(palavra) > 4
]

print(new_words) # ['PYTHON', 'LINGUAGEM', 'PODEROSA', 'SIMPLES']
