"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para replicar determinadas ações ao longo do código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def melhor():
    print('Neymar')

resposta = str(input('Quer saber qual o melhor jogador brasileiro do mundo? [S/N] ')).upper()
if 'S' in resposta:
    melhor()

else:
    print('Então vai cagar!')


# Funções com parâmetros
def calculo(a, b, c): # Parâmetros
    print('A soma dos valores é', a+b+c)
    print('O produto dos valores é', a*b*c)
    print(f'Portanto, {a} + {b} + {c} =', a+b+c)
    print(f'{a}*{b}*{c} = ', a*b*c)

reais = []

escolha = str(input('Deseja ver a função CÁLCULO funcionando? [s/n]')).lower()
if 's' in escolha:
    for i in range(0, 3):
        n = float(input('Digite um número real: '))
        reais.append(n)
    
    x, y, z = reais

    calculo(x, y, z) # Argumentos

else:
    print('Estraga prazer, em...')


def saudacao(nome):
    print(f'Olá, mestre {nome}!')

nome = str(input("What's your name? "))
saudacao(nome)


# E se eu não quiser passar um argumento ao meu parâmetro?
def subtracao(a = 5, b = 1):
    print(f'{a} - {b} = {a - b}')

subtracao() # Se eu não passar nenhum valor, a função trabalha com o que ela já tem

subtracao(100, 54) # Se eu passar valores, a função trabalha com os valores passados

subtracao(4) # 4 - 1 = 3 -> utilizou apenas o valor que passei com o que já tinha
