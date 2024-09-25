import os

os.system("cls")

# EXEMPLO 1
print("\n[1] Sacar\n[2] Extrato\n[0] Sair")
vv = int(input("Escolha um valor: "))

match vv:
    case 0:
        print("Saindo...")
    case 1:
        print("Sacando...")
    case 2:
        print("Exibindo extrato...")
    case _:
        print("Opção inválida!")
