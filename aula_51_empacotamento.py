'''
Introdução ao Empacotamento e Desempacotamento
'''

nomes = ['Valktro', 'Nelvis', 'Stanley', 'Claudisdiney']
nome1, nome2, nome3, nome4 = nomes # Importante ter a mesma quantidade de valores e variáveis -> se não, dá erro de empacotamento/desempacotamento
print(nome1, nome2, nome3, nome4) # Valktro Nelvis Stanley Claudisdiney

# E se eu quiser apenas algum(s) item(s) da lista?
idades = [26, 33, 47, 18]
idade1, *resto = idades
print(idade1, resto) # 26 [33, 47, 18] -> uma outra lista foi gerada com o restante dos valores
*inicial, ultimo = idades
print(inicial, ultimo) # [26, 33, 47] 18
primeiro, *meio, nao_primeiro = idades
print(primeiro, meio, nao_primeiro) # 26 [33, 47] 18
first, second, *other_things = idades
print(first, second, other_things) # 26 33 [47, 18]

# E quando eu não quero usar a variável "resto"?
sobrenomes = ['André', 'Liberato', 'Magalhães']
sobrenome1, *_ = sobrenomes
print(sobrenome1) # André
print(_) # ['Liberato', 'Magalhães'] -> a variável existe, mas essa é uma forma de dizer a outros devs que eu não quero usá-la para nada
_, sobrenome2, _ = sobrenomes
print(sobrenome2) # Liberato
