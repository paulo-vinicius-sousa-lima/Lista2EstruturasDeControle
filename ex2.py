import math

hora = int(input("Digite a hora: "))
chuva = int(input("Chuva? (0 ou 1): "))
fluxo = int(input("Fluxo: (0 baixo, 1 médio, 2 alto): "))

if (7 <= hora <= 9) or (17 <= hora <= 19):
    tempo = 60
else:
    tempo = 35

if chuva == 1:
    tempo += tempo * 0.2

if fluxo == 2:
    tempo += 15
elif fluxo == 0:
    tempo -= 10

tempo = math.ceil(tempo)

print(f"Tempo: {tempo}")
