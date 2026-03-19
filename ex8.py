n = int(input("Digite n (obrigatorio: n > 0): "))

if n <= 0:
    print("Erro: n tem que ser maior que zero.")
else: 
    somaDivisores = 0

    for i in range(1, n):
        if n % i == 0:
            somaDivisores += i

    print(f"Soma dos divisores: {somaDivisores}")

    if somaDivisores == n:
        print("Classificacao: perfeito")
    elif somaDivisores > n:
        print("Classificacao: abundante")
    else:
        print("Classificacao: deficiente")
