'''
Argumentos nomeados (não posicionais) e não nomeados (posicionais) em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

# Argumentos não nomeados
def soma(x, y):
    # Definição
    print(f'{x = } e y = {y} | x + y =', x + y)

soma(5, 11) # x = 5 e y = 11 | x + y = 16


# Argumentos nomeados
def subtracao(x, y):
    print(f'{x} - {y} =', x - y)

subtracao(y = 11, x = 7) # 7 - 11 = -4

'''
Você pode nomear e não nomear argumentos (não aconselhável) em uma 
mesma função, porém à partir do momento que você nomear um argumento, 
você precisa nomear os próximos.
'''
