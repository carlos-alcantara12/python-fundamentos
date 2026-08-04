
# CONSTANTE = "Variáveis" que não vão mudar
# Muitas condições num mesmo if (ruim)
# O código deve ser o mais objetivo e clean possível

RADAR_1 = 60      # velocidade máxima do radar 1
LOCAL_1 = 100     # local onde o radar 1 está
RADAR_RANGE = 1   # a distância onde o radar pega

# CORRIGIDO: as variáveis 'velocidade' e 'local_carro' não existiam antes,
# o que causava NameError assim que o código tentava usá-las.
velocidade = float(input("Digite a velocidade do carro: "))
local_carro = float(input("Digite a posição do carro: "))

vel_carro_pass_radar_1 = velocidade > RADAR_1

# CORRIGIDO: comparação dupla (a <= x <= b) no lugar do 'and' encadeado,
# mais legível pra expressar "está dentro de um intervalo".
carro_passou_radar_1 = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1')
