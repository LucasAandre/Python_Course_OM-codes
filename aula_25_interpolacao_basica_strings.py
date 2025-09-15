'''
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
'''

"""
Relembrando outras oupções:
print('Você digitou {} números'.format(variavel))

OU

print(f'Você digitou {variavel} números')
"""

nome = str(input('Digite seu nome: '))
peso = float(input('Qual o seu peso? '))
variavel = '%s, seu peso é %.2f' % (nome, peso)
print(variavel)

escolha = str(input('Deseja aprender sobre HEXADECIMAL? [S/N] ')).upper()

if escolha == 'S':
    inteiro = int(input('Digite um número inteiro: '))
    print('O hexadecimal de %d é %04X' % (inteiro, inteiro)) # 4 casas no hexadecimal (preenchendo com 0)

elif escolha == 'N':
    print('Ok, até mais...')

else:
    print('Você não sabe ler?')