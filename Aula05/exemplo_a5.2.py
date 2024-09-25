import os

os.system("cls")

# EXEMPLO 2
print("\n[0] Manhã\n[1] Tarde\n[2] Noite")
numero=int(input("Informe o número do turno: "))

match numero:
    case 0:
        print("Manhã")
    case 1:
        print("Tarde")
    case 2:
        print("Noite")
    case _:
        print("Valor inválido")
