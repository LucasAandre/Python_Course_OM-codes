# While Continue

contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        continue # Faz com que retorne ao início do laço, sem rodar o que vem abaixo (print)

    print(contador)

    if contador == 9:
        break


'''
1
2
3
4
5
7
8
9
'''