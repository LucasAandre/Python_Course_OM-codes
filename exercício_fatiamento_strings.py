nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.') 

    novo_nome = nome.replace(' ', '') # Remove os espaços

    print(f'Seu nome tem {len(novo_nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]} e a última letra do seu nome é {nome[-1]}')
    print(nome[0:4]) # No caso de Lucas: Luca
