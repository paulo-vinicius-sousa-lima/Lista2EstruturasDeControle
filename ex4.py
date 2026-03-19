lista = [
    "Casa", 
    "Sol", 
    "Amizade", 
    "Livro", 
    "Janela",
    "Caminho", 
    "Esperança", 
    "Mar", 
    "Montanha", 
    "Tempo",
    "Sorriso", 
    "Música", 
    "Coração", 
    "Vento", 
    "Luz",
    "Flor", 
    "Noite", 
    "Sonho", 
    "Liberdade", 
    "Universo"
]

palavra = input("Qual palavra você deseja buscar? ")

encontrada = False

for i, item in enumerate(lista):
    if palavra.lower() == item.lower():
        print(f"Índice da palavra: {i}")
        encontrada = True
        break

if not encontrada:
    print("Palavra não encontrada.")
