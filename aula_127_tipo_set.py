'''
Sets - Conjuntos em Python (tipo set)

Conjuntos são ensinados na matemática

Representados graficamente pelo diagrama de Venn

Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.


Criando um set
set (iterável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados de iteráveis.

- eles não tem índexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard

Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^- itens que não estão em ambos
'''

s1 = set('Lucas')
print(s1) # {'L', 's', 'a', 'c', 'u'}

s2 = set()
print(s2) # set()

s3 = {1, 'Lucas', 3}
print(s3) # {1, 3, 'Lucas'}

s4 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s4) # {1, 2, 3}
print(5 in s4) # False

d1 = {} # Isso é um dicionário
s5 = set() # Isso é um set


# add
s5.add('Neymar')
s5.add(11)
print(s5) # {11, 'Neymar'}

# update
s5.update('Olá mundo!')
print(s5) # {'d', '!', 'O', 'u', 11, 'n', 'á', 'l', 'Neymar', ' ', 'o', 'm'}
s5.update(('Give me money', 21))
print(s5) # {'!', 'á', 11, 'n', 'o', 'd', 21, 'u', 'l', 'Neymar', 'O', 'm', 'Give me money', ' '}

# clear
s4.clear()
print(s4) # set()

# discard
s5.discard('Give me money')
print(s5) # {'n', 'l', ' ', 'u', 11, 'Neymar', 'm', 'O', 21, 'á', 'd', '!', 'o'}


# Operadores

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # União
print(s3) # {1, 2, 3, 4}

s3 = s1 & s2 # Intersecção
print(s3) # {2, 3}

s3 = s1 - s2
print(s3) # {1} --> se eu tivesse colocado na ordem inversa, apareceria {4}

s3 = s1 ^ s2
print(s3) # {1, 4}


# Exemplo de uso dos sets

letras = set()
while True:
    letra = str(input('Digite uma letra: ')).lower()
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns, você digitou a letra premiada!')
        break

    print(letras)
