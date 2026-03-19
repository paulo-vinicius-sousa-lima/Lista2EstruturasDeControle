a = int(input("Digite a: "))
b = int(input("Digite b: "))
p = int(input("Digite p: "))

if p == 0:
    print("Erro: passo p nao pode ser zero.")
elif a < b and p <= 0:
    print("Erro: p deve ser positivo.")
elif a > b and p >= 0:
    print("Erro: p deve ser negativo.")
else:
    valoresImpressos = 0
    
    if p > 0:
        fim = b + 1
    else:
        fim = b - 1
    
    for i in range(a, fim, p):
        print(i)
        valoresImpressos += 1

    print(f"Quantidade de valores impressos: {valoresImpressos}")
