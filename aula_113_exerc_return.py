'''
EXERCÍCIOS COM FUNÇÕES

1. Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o 
total para uma variável e mostre o valor da variável.

2. Crie uma função que diga se um número é par ou ímpar. Retorne se o número é par ou 
ímpar.
'''

# Exercício 1
def mult(*args):
    total = 1

    for i, num in enumerate(args):
        total *= num
        if i < len(args) - 1:
            print(num, end= ' * ')
        
        else:
            print(num, end= ' = ')

    return total

c = 0

numeros = []

print('==== EXERCÍCIO 01 ====\n')
escolha = int(input('Digite a quantidade de números que você deseja adicionar na conta: '))

while c < escolha:
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)
    c += 1
    
result = mult(*numeros)

print(result)


# Exercício 2
def valid(x):
    
    if x % 2 == 0:
        result = 'Esse número é par'
    
    else:
        result = 'Esse número é ímpar'
    
    return result

print('\n')

print('==== EXERCÍCIO 02 ====\n')
num = int(input('Digite um número: '))

conta = valid(num)

print(conta)
