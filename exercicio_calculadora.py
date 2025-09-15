"""
Calculadora com While

1. Pedir os valores ao usuário (2 valores);
2. Pedir o operador ao usuário;
3. Realizar a operação matemática entre eles;
4. Obrigatório o uso do While
"""

print('MATEMÁTICA NÃO RIO! (quem pegou, pegou!)\n\n')

try:
    n1 = float(input('Digite o 1º número: '))
    n2 = float(input('Digite o 2º número: '))

except:
    print('Somente números são aceitos!')

print('\n[+] SOMA\n[-] SUBTRAÇÃO\n[*] MULTIPLICAÇÃO\n[/] DIVISÃO\n[N] NOVOS NÚMEROS\n[S] SAIR')
escolha = str(input('\nQual a sua escolha? ')).upper()
print('\n')

while escolha != 'S':

    if escolha == '+':
        soma = n1 + n2
        print(f'{n1:.2f} + {n2:.2f} = {soma:.2f}')

        escolha = str(input('\nEscolha outra opção: ')).upper()
    
    elif escolha == '-':
        subtracao = n1 - n2
        print(f'{n1:.2f} - {n2:.2f} = {subtracao:.2f}')

        escolha = str(input('\nEscolha outra opção: ')).upper()
    
    elif escolha == '*':
        multiplicacao = n1 * n2
        print(f'{n1:.2f} * {n2:.2f} = {multiplicacao:.2f}')

        escolha = str(input('\nEscolha outra opção: ')).upper()
    
    elif escolha == '/':
        divisao = n1 / n2
        print(f'{n1:.2f} / {n2:.2f} = {divisao:.2f}')

        escolha = str(input('\nEscolha outra opção: ')).upper()
    
    elif escolha == 'N':
        try:
            n1 = float(input('\nDigite o 1º número: '))
            n2 = float(input('Digite o 2º número: '))

            escolha = str(input('\nEscolha outra opção: ')).upper()
    
        except:
            print('Somente números são aceitos!')

    else:
        print('Opção inválida!')
        escolha = str(input('\nEscolha outra opção: ')).upper()

print('\nObrigado por usar nossos serviços!')


    





