sair = False
estado = "fechado"

while not sair:

    print("""
    ********************************
    ************* MENU *************
    *** (A) → abrir atendimento  ***
    *** (T) → triagem            ***
    *** (E) → encaminhar         ***
    *** (F) → finalizar          ***
    *** (S) → sair               ***
    ********************************
    ********************************   
    """)

    print(f"Estado atual: {estado}")
    
    comando = input("Digite o comando: ").upper()

    match comando:
        case "A":
            if estado == "fechado":
                estado = "aberto"
                print("Atendimento aberto!")
            else:
                print("Erro: atendimento ja esta aberto ou em andamento.")

        case "T":
            if estado == "aberto":
                estado = "triado"
                print("Atendimento triado!")
            else:
                print("Erro: so pode triar apos abrir.")

        case "E":
            if estado == "triado":
                estado = "encaminhado"
                print("Atendimento encaminhado!")
            else:
                print("Erro: so pode encaminhar após triagem.")

        case "F":
            if estado == "encaminhado":
                estado = "fechado"
                print("Atendimento finalizado!")
            else:
                print("Erro: so pode finalizar apos encaminhamento.")

        case "S":
            print("Saindo do sistema...")
            sair = True

        case _:
            print("Comando invalido!")

