'''
GERANDO O PRIMEIRO DÍGITO DE UM CPF (***.***.***-AB) --> A: 1º dígito e B: 2º dígito
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
Multiplicando cada um dos valores por uma contagem regressiva começando em 10

Ex:

746.824.890-70 (746824890)
  10  9  8  7  6  5  4  3  2
*  7  4  6  8  2  4  8  9  0
  70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado anterior por 10:
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11:
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0 

Contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7, ou seja, o CPF informado é válido (pelo menos, por enquanto)
'''

print('==== VALIDADOR DE CPF ====\n')

c = 0
m = 10
soma = 0
cpf = []

for i in range(1, 10):
    while True:
      try:
          r = int(input(f'Digite o {i}º número do seu CPF: '))
          cpf.append(r)
          soma += (r * m)
          m -= 1
          break # Entrada válida. Sai do while e volta ao for.
      
      except ValueError:
          print('Somente números inteiros são aceitos! Tente novamente.')

produto = soma * 10
resto = produto % 11

digito1 = 0 if resto > 9 else resto

# Converte todos os números para string e junta tudo
juntos = ''.join(str(n) for n in cpf)

blocos = []

# Percorre a string de 3 em 3 e adiciona os blocos
for i in range (0, len(juntos), 3):
    bloco = juntos[i:i+3] # Pega do índice i até o i+3 e salva em uma variável
    blocos.append(bloco)

# Junta os blocos com pontos
resultado = '.'.join(blocos) # A função '.'.join(...) pega uma lista de strings (no caso, a lista blocos) e junta tudo com ponto entre os elementos

print('Os 9 primeiros números do seu CPF são:', resultado)
print(f'O 1º dígito do seu CPF é: {digito1}')
