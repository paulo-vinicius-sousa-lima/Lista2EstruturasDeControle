s = input("Digite uma string: ")

sLimpa = ""

for c in s:
    if c.isalnum():
        sLimpa += c.lower()

if sLimpa == sLimpa[::-1]:
    print("Eh palindromo")
else:
    print("Nao eh palindromo")
