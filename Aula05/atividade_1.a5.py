import os

os.system("cls")

# ATIVIDADE 1
print(30*"_")
print("ATIVIDADE 1")
mes = int(input("Digite um número de 1 a 12: "))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Mês inválido.")

# ATIVIDADE 2
print(30*"_")
print("ATIVIDADE 2")
print("Escolha um tipo de restaurante:\n- Chinês\n- Italiano\n- Mexicano\n- Vegetariano")
rest = input("Digite o seu tipo de restaurante: ")[0].upper()

match rest:
    case "C":
        print("Tente o Yakissoba!")
    case "I":
        print("Tente a Pizza!")
    case "M":
        print("Tente o Taco!")
    case "V":
        print("Tente o Hambúrguer de Tofu!")
    case _:
        print("Fique com fome!")

# ATIVIDADE 3
print(30*"_")
print("ATIVIDADE 3")

number = float(input("Bem vindo! Digite um valor: "))

print(f"Número escolhido: {number}")

op = int(input("\nAgora escolha uma opção abaixo:\n1. Adicionar Item\n2. Remover Item\n3. Listar Items\n4. Sair\n"))

match op:
    case 1:
        number += 1
        print(number)
    case 2:
        number -= 1
        print(number)
    case 3:
        print("I " * int(number))
    case 4:
        pass
    case _:
        print("Opção inválida.")
