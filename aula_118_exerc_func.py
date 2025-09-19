'''
Crie funções que duplicam, triplicam e quadruplicam o número recebido como
parâmetro.
'''

print('==== EXERCÍCIO DE FUNÇÕES ====\n')

def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

def quadruplo(x):
    return x * 4

while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        break

    except ValueError:
        print('Aceitamos apenas números inteiros!')

mult_2 = dobro(numero)
mult_3 = triplo(numero)
mult_4 = quadruplo(numero)

print(f'O dobro de {numero} é {mult_2}')
print(f'O triplo de {numero} é {mult_3}')
print(f'O quadruplo de {numero} é {mult_4}')


# Solução do professor Otávio Miranda:
print('\n\n')

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f'O dobro de {numero} é {duplicar(numero)}')
print(f'O triplo de {numero} é {triplicar(numero)}')
print(f'O quadruplo de {numero} é {quadruplicar(numero)}')
