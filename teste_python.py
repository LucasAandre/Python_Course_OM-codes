# Função que retorna a soma entre dois números
def soma(x, y):
    soma = (x + y)
    print(f'{x} + {y} = {soma}')

print('==== QUESTÃO 1 ====\n')
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

soma(n1, n2)


'''
Escreva um programa que percorra os números de 1 a 100 e imprima 'Fizz' para múltiplos de 3,
'Buzz' para múltiplos de 5 e 'FizzBuzz' para múltiplos de ambos.
'''
print('\n')
print('==== QUESTÃO 2 ====\n')

numeros = list(range(1, 101))

for i in numeros:
    if i % 3 == 0:
        if i % 5 == 0:
            print(f'{i} - FizzBuzz')
        else:
            print(f'{i} - Fizz')
    
    elif i % 5 == 0:
        print(f'{i} - Buzz')

'''
Escreva um código que peça a idade do usuário e diga se ele é menor de idade ou maior de idade.
'''
print('\n')
print('==== QUESTÃO 3 ====\n')

from datetime import datetime

ano_nascimento = int(input('Digite o ano de seu nascimento: '))
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade >= 18:
    print(f'Você tem {idade} anos e já é maior de idade.')

else:
    print(f'Você tem {idade} anos e não é maior de idade.')


'''
Dada a string 'banana', escreva um código que conte quantas vezes a letra 'a' aparece.
'''
print('\n')
print('==== QUESTÃO 4 ====\n')

string = 'banana'

print('Na palavra "banana" a letra "a" aparece', string.count('a'), 'vezes')


'''
Dada a lista [10, 20, 30, 40, 50], escreva um código que:
   - some todos os elementos,
   - calcule a média,
   - encontre o maior e o menor valor.
'''
print('\n')
print('==== QUESTÃO 5 ====\n')

valores = [10, 20, 30, 40, 50]

soma2 = sum(valores)
media = soma2 / len(valores)
maior = max(valores)
menor = min(valores)

print(f'Na lista {valores}, a soma é {soma2}, a média é {media}, o maior valor da lista é {maior} e o menor é {menor}')
