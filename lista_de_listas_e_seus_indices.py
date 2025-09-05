'''
Lista de listas e seus índices
'''

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine',], # 1
    # 0       1       2         3
    ['Luiz', 'João', 'Eduarda', (47, 1, 98, -3, 45)] # 2
]

print(salas[1][0]) # Elaine
print(salas[0][1]) # Helena
print(salas[2][3][2]) # 98
