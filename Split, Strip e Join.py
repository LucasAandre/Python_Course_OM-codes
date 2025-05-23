'''
split e join com list e str
split - divide uma string
join - une uma string
'''

# split()
frase = 'Olha só, que coisa interessante'

lista_palavras = frase.split()
print(lista_palavras) # ['Olha', 'só,', 'que', 'coisa', 'interessante']

lista_palavras2 = frase.split(',')
print(lista_palavras2) # ['Olha só', ' que coisa interessante']

# strip()
frase2 = '   Oilá,   amigos!   '

leitura1 = frase2.strip() # Remove os espaços das extremidades da string
print(leitura1) # Oilá,   amigos!

leitura2 = frase2.rstrip() # Remove os espaços da direita
print(leitura2) #    Oilá,   amigos!

leitura3 = frase2.lstrip() # Remove os espaços da esquerda
print(leitura3) # Oilá,   amigos!  


frase3 = '   Eita   ,   que confusão!   '
lista_frases_cruas = frase3.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas) # ['   Eita   ', '   que confusão!   ']
print(lista_frases) # ['Eita', 'que confusão!']


# join()
frases_unidas = '-'.join('ABC')
print(frases_unidas) # A-B-C

frases_unidas2 = '*'.join(lista_frases)
print(frases_unidas2) # Eita*que confusão!
