"""
Qual letra apareceu mais vezes na frase? (Iterando strings com while)
"""

frase = 'O Python é uma linguagem de programação' \
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum'

print(frase.count('Python')) # 2
print(frase.count('o')) # 9

i = 0

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

# Codificando qual a letra que mais se repetiu:
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    
    print(letra_atual, qtd_apareceu_mais_vezes_atual)
    i += 1

print(f'\nA letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes.upper()}", que apareceu {qtd_apareceu_mais_vezes}x')