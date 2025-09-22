# Exercício - Sistema de Perguntas e Respostas

from time import sleep
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '2', '4', '6'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['1', '50', '11', '25'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['5', '44', '10', '1'],
        'Resposta': '5',
    },
]

# Deixar essas vírgulas finais é opcional e trata-se de uma boa prática entre os devs

'''
1. O usuário verá a pergunta e as alternativas;
2. Se ele escolher a resposta correta, aparecerá uma mensagem;
3. Se ele escolher a resposta errada, aparecerá outra mensagem.
'''

def primeira(nome):
    print(f'{nome}, {perguntas[0]['Pergunta']}')
    
    c = 0

    for i in perguntas[0]['Opções']:
        print(f'{c+1}) {perguntas[0]['Opções'][c]}')
        c += 1
    
    # Para usar o dicionário completo e não a alternativa
    resposta = str(input('Digite aqui o valor correto (e não alternativa): '))

    if resposta == perguntas[0]['Resposta']:
        resultados.append('Acerto')
        return 'Resposta certa!'
    
    else:
        resultados.append('Erro')
        return 'Resposta errada!'

def segunda(nome):
    print(f'{nome}, {perguntas[1]['Pergunta']}')
    
    c = 0

    for i in perguntas[1]['Opções']:
        print(f'{c+1}) {perguntas[1]['Opções'][c]}')
        c += 1
    
    # Para usar o dicionário completo e não a alternativa
    resposta = str(input('Digite aqui o valor correto (e não alternativa): '))

    if resposta == perguntas[1]['Resposta']:
        resultados.append('Acerto')
        return 'Resposta certa!'
    
    else:
        resultados.append('Erro')
        return 'Resposta errada!'

def terceira(nome):
    print(f'{nome}, {perguntas[2]['Pergunta']}')
    
    c = 0

    for i in perguntas[2]['Opções']:
        print(f'{c+1}) {perguntas[2]['Opções'][c]}')
        c += 1
    
    # Para usar o dicionário completo e não a alternativa
    resposta = str(input('Digite aqui o valor correto (e não alternativa): '))

    if resposta == perguntas[2]['Resposta']:
        resultados.append('Acerto')
        return 'Resposta certa!'
    
    else:
        resultados.append('Erro')
        return 'Resposta errada!'

# Criando uma lista para arquivar os resultados
resultados = []

print('==== SHOW DO MILHINHO ====\n\n')

nome = str(input('Digite seu nome: '))

# print(perguntas[0]['Opções'][2])

# Uma pequena brincadeira (não pode faltar)
while True:
    escolha = str(input('Está preparado para o jogo? [SIM / NÃO] ')).upper()
    
    if 'N' in escolha:
        print('\nEntão está fazendo o que aqui?\nVou perguntar de novo...\n')
        sleep(2)
    
    else:
        print('\nAgora sim!')
        break

os.system('clear')

# Chamando a primeira pergunta
print('Primeira pergunta:\n')
print(primeira(nome))
sleep(2)

os.system('clear')

# Chamando a segunda pergunta
print('Segunda pergunta:\n')
print(segunda(nome))
sleep(2)

os.system('clear')

# Chamando a terceira pergunta
print('Terceira pergunta:\n')
print(terceira(nome))
sleep(2)

acertos = 0
erros = 0

for resultado in resultados:
    if resultado == 'Acerto':
        acertos += 1
    
    else:
        erros += 1

os.system('clear')

print(f'{nome}, você teve {acertos} acerto(s) e {erros} erro(s).')
print('\nAté a próxima!')
