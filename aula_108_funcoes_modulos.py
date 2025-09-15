"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# Função chamada "escopo" apenas para ficar de fácil entendimento
def escopo():
    x = 11 # Escopo da função
    print(x)

# Executando (chamando) a função, a variável criada na função (x) aparecerá
escopo()

# Caso eu queira chamar a variável x fora do escopo (fora da função), ela não aparecerá
# print(x) # Erro - name 'x' is not defined

# Isso, pois a função tem seu próprio escopo

# Eu posso definir a variável em um escopo externo:

y = 11 # Escopo do módulo

def escopo2():
    print(y) # Escopo da função

escopo2() # 11

z = 17 # Escopo do módulo

def escopo3():
    def escopo4():
        print(z) # Acesso a variável z que está definida no escopo do módulo
    print(z) # Acesso a variável z que está definida no escopo do módulo

escopo3() # 17

l = 101

def escopo5():
    def escopo6():
        p = 215
        print(l, p)
    
# escopo6() # NameError: name 'escopo6' is not defined. Did you mean: 'escopo'? -> pois a função 6 só pode ser executada se a função 5 for executada

# Solução:

def escopo7():
    def escopo8():
        p = 299
        print(l, p)
    
    escopo8()

escopo7() # 101 299


t = 449 # Escopo global

def escopo9():
    t = 45 # Escopo local

    def escopo10():
        a = 22
        print(t, a)

    escopo10()
    print(t)

escopo9() # 45, 22

# 45

print(t) # 449


# Uma má prática da programação é editar variáveis do escopo global dentro de escopos locais:

var = 10

def function():
    global var # Estou dizendo que a próxima edição no var deve ser tratado como GLOBAL
    var = 'Lucas'

    def other_function():
        var = False
        print('Jujuba', var)
    
    other_function()
    print(var) # Lucas -> seguindo o escopo local (que se tornou global)

print(var) # 10 -> a função ainda não foi executada
function() # Jujuba False -> seguindo o escopo local
print(var) # Lucas -> seguindo o novo escopo global
