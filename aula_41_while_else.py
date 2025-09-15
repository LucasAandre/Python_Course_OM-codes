# While / else

string = 'Neymar'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1

else:
    print('Fim do loop.')

# Se eu colocar um break no while, o else não é executado.
# Ou seja, essa bosta não serve para nada!