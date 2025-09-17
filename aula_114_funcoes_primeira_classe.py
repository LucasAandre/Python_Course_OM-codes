'''
Higher Order Functions
Funcções de Primeira Classe
'''

def saudacao(msg):
    return msg

v = saudacao('Bom dia')
print(v) # Bom dia


# Uma função executando outra
def executa(funcao):
    return funcao('Oilá')

x = executa(saudacao)

print(x) # Oilá

# Ou
def executa2(funcao, msg):
    return funcao(msg)

y = executa2(saudacao, 'Nelvis')

print(y) # Nelvis


# Vários parâmetros
def saudacao2(msg, outros):
    return f'{msg}, {outros}!'

def executa3(funcao, *args):
    return funcao(*args)

print(
    executa3(saudacao2, 'Bom dia', 'Lucas') # Bom dia, Lucas!
)

print(executa3(saudacao2, 'Boa noite', 'Neymar')) # Boa noite, Neymar!
