# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
# Ou
# iterator = iter(iterable)

print(next(iterator)) # Eu
print(next(iterator)) # tenho
print(next(iterator)) # __iter__

print()

# Generator são funções que sabem pausar
# Iterator é uma classe que precisa ter os métodos iter e next
# Iterator geralmente trabalha com um iterável
# Todo generator é um iterator
# Um iterator não é um generator
# Iterator você não usa direto
# Generator é uma função que pausa em algum lugar

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(generator) # <generator object <genexpr> at 0x729927908a00>

# Vendo o tamanho da lista e do generator, em bytes
print(sys.getsizeof(generator)) # 192
print(sys.getsizeof(lista)) # 85176

'''
A lista (um iterável) é muito mais pesada do que um generator, pois ela salva TODOS os valores na memṕria.
Já o generator salva um por vez.
'''

print(next(generator)) # 0
print(next(generator)) # 1
print(next(generator)) # 2
print(next(generator)) # 3

'''
A vantagem da lista é que como todos os elementos estão salvos na memória, eu consigo acessar TODOS os índices quando eu quiser:
lista[999], lista[-1] e etc

No generator eu não consigo nem usar o len(), pois ele não salva os elementos na memória.
'''
