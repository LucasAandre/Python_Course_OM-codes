'''
Cuidados com dados mutáveis

- Copiando valor (imutáveis)
- Apontando valor (mutáveis)
'''

# Quando quero apontar para o mesmo valor
lista_a = ['Lucas', 'Pamela', 'Neymar']
lista_b = lista_a
lista_a[2] = 'Messi'

print(lista_b) # ['Lucas', 'Pamela', 'Messi']

# Quando quero copiar o valor de uma variável para outra
lista_c = ['André', 'Liberato', 'Junior']
lista_d = lista_c.copy()
lista_c[2] = 11

print(lista_d) # ['André', 'Liberato', 'Junior']
