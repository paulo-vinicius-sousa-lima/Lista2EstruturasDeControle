s1 = input("Digite a primeira palavra/frase: ")
s2 = input("Digite a segunda palavra/frase: ")

limpa1 = ""
limpa2 = ""

for c in s1:
    if c.isalnum():  
        limpa1 += c.lower()

for c in s2:
    if c.isalnum():
        limpa2 += c.lower()

ord1 = sorted(limpa1)
ord2 = sorted(limpa2)

if ord1 == ord2:
    print("São anagramas")
else:
    print("Não são anagramas")
    