'''
GERANDO O SEGUNDO DÍGITO DE UM CPF (***.***.***-AB) --> A: 1º dígito e B: 2º dígito
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO,
Multiplicando cada um dos valores por uma contagem regressiva começando em 11

Ex:

746.824.890-70 (746824890)
  11 10  9  8  7  6  5  4  3  2
*  7  4  6  8  2  4  8  9  0  7 <-- 1º dígito
  77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77 + 40 + 54 + 64 + 14 + 24 + 36 + 0 + 14 = 363

Multiplicar o resultado anterior por 10:
363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11:
3630 % 11 = 0

Se o resultado anterior for maior que 9:
    resultado é 0 

Contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
'''

print('==== VALIDADOR DE CPF_v2 ====\n')

c = 0
m = 10
soma = 0
cpf = []
x = 11
soma2 = 0
cpf2 = list()

for i in range(1, 10):
    while True:
      try:
          r = int(input(f'Digite o {i}º número do seu CPF: '))
          cpf.append(r)
          soma += (r * m)
          m -= 1
          cpf2.append(r)
          soma2 += (r * x)
          x -= 1
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

# Cálculo do 2º dígito
soma2 += (digito1 * 2)
produto2 = soma2 * 10
resto2 = produto2 % 11

if resto2 > 9:
    digito2 = 0

else:
    digito2 = resto2

print(f'O 2º dígito do seu CPF é: {digito2}')

# Salva os dígitos em uma nova lista
digitos = [digito1, digito2]

# Transforma os dígitos em strings
digitos_str = [str(y) for y in digitos]

# Junta os elementos da lista em uma única string
resultado2 = ''.join(digitos_str)

# Formata o CPF
cpf3 = resultado + '-' + resultado2

print('\nPortanto, seu CPF completo é:', cpf3)
