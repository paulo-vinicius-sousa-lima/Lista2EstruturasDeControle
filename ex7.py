n = int(input("Entre com n: "))

if n < 0:
    print("Erro!")
else:
    fatorial = 1

    for k in range(1,n + 1):
        fatorial *= k

        if fatorial > 1_000_000:
            print(f"Passou do limite em {k}!")
            print(f"Valor acumulado: {fatorial}")
            break
    else:
        print(f"{n}! = {fatorial}")
