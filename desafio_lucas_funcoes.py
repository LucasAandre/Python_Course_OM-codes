'''
DESAFIO DO LUCAS

Crie um serviço de atendimento utilizando funções.
'''

print('==== ATENDIMENTO GRIL NOTA MIL ====\n')

#Declaração de listas
pedido =[]
precos = []


# Função cardápio
def cardapio():
    print('\n')
    print('Escolha seu prato:')
    escolha_cardapio = int(input('1. Pizza [R$100,00]\n2. Lasanha [R$80,00]\n3. Frango à Parmegiana [R$25,00]\n4. Salada [R$20,00]\n5. Sair\n'))

    print('\n')

    # Condição da escolha do usuário
    if escolha_cardapio == 1:
        print('Você escolheu pizza!')
        pedido.append('Pizza')
        precos.append(100)
        print('Redirecionando ao menu.')
    
    elif escolha_cardapio == 2:
        print('Você escolheu lasanha!')
        pedido.append('Lasanha')
        precos.append(80)
        print('Redirecionando ao menu.')
    
    elif escolha_cardapio == 3:
        print('Você escolheu frango à parmegiana!')
        pedido.append('Frango à Parmegiana')
        precos.append(25)
        print('Redirecionando ao menu.')
    
    elif escolha_cardapio == 4:
        print('Você escolheu salada!')
        pedido.append('Salada')
        precos.append(20)
        print('Redirecionando ao menu.')

    elif escolha_cardapio == 5:
        print('Você escolheu sair!')
        print('Redirecionando ao menu.')
    
    else:
        print('\n')
        print('Opção inexistente!\n')
        print('Redirecionando ao menu.')

    # Chamada da função menu (que se encontra abaixo da função cardápio)
    menu()

# Função conta
def conta():
    print('\n')
    print('Seu pedido foi:')
    for i, prato in enumerate (pedido, start=1): # Exibição do pedido do cliente
        preco = precos[i-1]
        print(f'{i}. {prato} - R${preco:.2f}')
    
    # Cálculo da conta total
    total = sum(precos)
    print(f'O total da sua conta é: R${total:.2f}')

# Função menu
def menu():
    print('\n')
    print('Escolha uma opção abaixo:\n')

    # Leitura e validação da escolha do cliente
    while True:
        try:
            escolha_menu = int(input('1. Cardápio\n2. Conta\n3. Sair\n'))
            break
        
        except ValueError:
            print('Apenas as opções acima são válidas.')
        
    if escolha_menu == 1:
        cardapio()
    
    elif escolha_menu == 2:
        conta()
    
    else:
        print('Volte sempre!')

# Dados iniciais, porém, declarados ao final do código (caso contrário, o código não funcionava)
nome = str(input('Olá, digite seu nome: '))
print(f'\nSeja bem-vindo, {nome}!')
print('\nVocê será direcionado ao menu do GRIL NOTA MIL.')

menu()
