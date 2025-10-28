'''
Introdução às Generator Functions em Python

generator = (n for n in range(1000000))
'''

def generator():
    yield 1 # pausar
    print('Continuando...')
    yield 2 # pausar
    return 'ACABOU'

gen = generator()
#print(generator()) # <generator object generator at 0x7eb908d84a90>
#print(next(gen)) # 1
#print(next(gen))
'''
Continuando...
2
'''

print()

for n in gen:
    print(n)
    '''
    1
    Continuando...
    2
    '''

# Outro exemplo de aplicação:
print()

def second_generator(n = 0, maximum = 10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

x = second_generator()

for i in x:
    print(i)
    '''
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    '''

# Sem o for, ficaria apenas no primeiro valor (0)

print()

y = second_generator(n = 5, maximum = 8)

for l in y:
    print(l)
    '''
    5
    6
    7
    8
    '''
