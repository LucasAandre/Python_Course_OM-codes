# No Python, quando queremos definir uma variável constante, ou seja, uma variável que não pode ter seu valor alterado, 
# definimos ela com letras MAIÚSCULAS

velocidade = 61 # Velocidade atual do carro
local_carro = 101 # Local em que o carro está na estrada (km)

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está (km)
RADAR_RANGE = 1 # A distância onde o radar pega

"""
Muitas condições no mesmo if não é legal
   <- Contagem de complexidade é ruim
"""

if velocidade > RADAR_1:
    print(f'Velocidade [{velocidade} km/h] acima do limite [{RADAR_1} km/h]!')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1: # \ -> indica quebra de linha
    print('Carro multado por excesso de velocidade!')

# Eu não teria feito dessa forma. Teria colocado o segund if dentro do primeiro if

# Solução do professor Otávio Miranda para deixar o código ainda mais "limpo":

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print(f'Velocidade [{velocidade} km/h] acima do limite [{RADAR_1} km/h]!')

if carro_multado_radar_1 and vel_carro_pass_radar_1: # Poderia colocar essa condição em uma variável e limpar ainda mais o código
    print('Carro multado por excesso de velocidade!')