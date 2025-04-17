menu = """

[d] = depositar
[s] = sacar
[e] = extrato
[q] = sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def saque():
    global saldo, extrato, numero_saques

    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários atingido.")
        return
    
    print("Quanto deseja sacar?: ")
    vs = float(input())

    if vs > limite:
        print("Valor excede o limite por saque.")
    elif vs > saldo:
        print("Saldo insuficiente.")
    elif vs <= 0:
        print("Valor inválido.")
    else:
        saldo -= vs
        numero_saques += 1
        extrato += f"Saque: R$ {vs:.2f}\n"
        print("Saque realizado com sucesso.")

def deposito():
    global saldo, extrato

    print("Quanto deseja depositar?: ")
    vd = float(input())
    saldo += vd
    extrato += f"Deposito: R$ {vd:.2f}\n"
    print("Depósito realizado com sucesso")

op = ""
    
while op != "q":
    
    op = input(menu)

    if op == "d":
        print("Deposito")
        deposito()

    elif op == "s":
        print("Saque")
        saque()

    elif op == "e":
        print("Extrato:")
        if extrato != "":
            print(extrato)
        else:
            print("Não foram realizadas movimentações")

    else:
        if op != "q":
            print("op invalida")

print("\nPrograma encerrado")


