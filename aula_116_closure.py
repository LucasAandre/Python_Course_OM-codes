'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar # Ao não colocar os () eu estou salvando os valores nela, mas não exibindo

s1 = criar_saudacao('Bom dia', 'Lucas')
s2 = criar_saudacao('Boa noite', 'Lucas')

print(s1) # <function criar_saudacao.<locals>.saudar at 0x76f7ac2dce00> --> endereço de memória da função

# Agora, com closure:
print(s2()) # Boa noite, Lucas!


# Se eu posso adiar a execução da função, eu também posso adiar passar os nomes:
def criar_saudacao2(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar # Ao não colocar os () eu estou salvando os valores nela, mas não exibindo

s3 = criar_saudacao2('Bom dia')

print(s3('Lucas')) # Bom dia, Lucas!

print(s3) # <function criar_saudacao2.<locals>.saudar at 0x7cbadf2bd3a0>

print(criar_saudacao2('Boa noite')('Neymar')) # Boa noite, Neymar!
