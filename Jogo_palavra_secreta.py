'''
JOGO DA PALAVRA SECRETA

Faça um jogo para o usuário adivinhar qual a palavra secreta:
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra por vez.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta, exiba a letra
- Se a letra digitada não estiver na palavra secreta, exiba *
- Faça a contagem de tentativas do seu usuário

Ex:
Palavra secreta: Neymar
Letra digitada pelo usuário: y
Terminal: **y***
'''

import time
import os
print('==== PALAVRA SECRETA! ====\n')
print('Preparando a palavra secreta...\n')
time.sleep(2) # Espera 2 segundos
print('Pronto! Palavra secreta escolhida. Vamos jogar!\n')

palavra = 'NEYMAR'
letras_corretas = ''
c = 0

while True:
    resposta = str(input('Digite uma letra que acredita constar na palavra secreta: ')).upper()
    c += 1

    if len(resposta) > 1:
        print('Digite apenas uma letra por vez!')
        continue

    if resposta in palavra:
        letras_corretas += resposta

    nova_palavra = ''
    
    for letra in palavra:
        if letra in letras_corretas:
            nova_palavra += letra
        
        else:
            nova_palavra += '*'
    
    print('Palavra formada:', nova_palavra)

    if nova_palavra == palavra:
        os.system('clear')
        print('VOCÊ VENCEU!')
        break

    escolha = str(input('Tem algum palpite de qual seja a palavra secreta? [S/N] ')).upper()

    if 'S' in escolha:
        palpite = str(input('Qual o seu palpite? ')).upper()

        if palpite == palavra:
            os.system('clear')
            print('VOCÊ VENCEU!')
            break

        else:
            print('\nAinda não... Vamos continuar jogando!\n')

print('\nA palavra secreta é:', palavra)
print(f'\nVocê usou {c} tentativas.')
print('\nJogo finalizado!')
