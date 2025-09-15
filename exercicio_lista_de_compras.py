'''
Faça uma lista de compras com listas.
- O usuário deverá ter a possibilidade de inserir,
apagar e listar valores da sua lista.
- Não permita que o programa quebre com erros de
índices inexistentes na lista.
'''

import os

print('==== LISTA DE COMPRAS AUTOMATIZADA ====\n')

lista = list() # Declarando a lista de compras

os.system('clear') # Limpando o terminal
nome = str(input('Digite seu nome: ')) # Extração do nome do usuário

while True:
   print('\n1. Ver lista de compras\n2. Adicionar item na lista\n3. Remover item da lista\n4. Sair\n') # Apresentando o menu

   escolha = int(input('Qual a sua escolha? ')) # Leitura da opção do usuário

   if escolha == 1:
      if not lista: # Se a lista estiver vazia
         os.system('clear') # Limpeza do terminal
         print('\nA lista de compras está vazia.')
      
      else:
         os.system('clear') # Limpeza do terminal
         print('\n---- LISTA DE COMPRAS ----')
         for i, item in enumerate(lista, start=1): # Exibição da lista completa
            print(f'{i}. {item}')
   
   elif escolha == 2:
      produto = str(input('\nDigite o nome do produto: '))
      print('\n')
      lista.append(produto) # Adição da string na lista
      print(produto, 'adicionado à lista!')
   
   elif escolha == 3:
      if not lista: # Se a lista estiver vazia
         os.system('clear') # Limpeza do terminal
         print('\nA lista de compras está vazia.')
         continue # Retorno ao início do loop
      
      os.system('clear') # Limpeza do terminal
      for i, item in enumerate(lista, start=1): # Exibição da lista completa
         print(f'{i}. {item}')
      
      try: # Tentativa
         escolha2 = int(input('\nDigite o número do item que deseja remover da lista: '))

         if 1 <= escolha2 <= len(lista): # Validação do índice digitado
            item_removido = lista[escolha2 - 1] # Salvamento da string antes de removê-la
            lista.pop(escolha2 - 1) # Remoção da string escolhida pelo usuário
            print(f'\n{item_removido} removido da lista!') # Exibição da string removida
         
         else:
            print('\nNúmero inválido!')
      
      except ValueError: # Se a tentativa der errado
         print('\nDigite um número válido!')
   
   elif escolha == 4:
      print('\nSaindo do programa.')
      break # Encerramento do loop

print('Até mais,', nome)
