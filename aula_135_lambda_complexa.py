def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# Fazendo a função soma através da função lambda:
print(
    executa(
        lambda x, y: x + y, 2, 3
    )
) # 5

# Ou:
print(executa(lambda *args: sum(args), 1, 2, 47, 56)) # 106

# Mesma coisa que:

print(executa(soma, 2, 3)) # 5


# Fazendo a função cria_multiplicador através da função lambda:
duplica = executa(lambda m: lambda n: n * m, 2) # Aqui eu defino que meu m = 2

print(duplica(11)) # 22

# Mesma coisa de:
triplica = cria_multiplicador(3)
print(triplica(11)) # 33

# OBS.: A função lambda é para coisas simples. Se está ficando complexo, não use lambda!
