'''
Desempacotamento em chamadas de funções
'''

string = 'ABCD'
lista = ['Lucas', 'André', 1, 2, 3, 'Silva']
tupla = 'Python', 'C++', 'Java'

for nome in lista:
    print(nome, end=' ') # Lucas André 1 2 3 Silva %

print('\n')

print(*lista) # Lucas André 1 2 3 Silva Lucas André 1 2 3 Silva
print(*string) # A B C D
print(*tupla) # Python C++ Java

print(*lista, sep='\n')
# Lucas
# André
# 1
# 2
# 3
# Silva
