from datetime import datetime
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    data = datetime.today()
    

    if opcao == "d":
        deposito = float(input("Digite o valor de depósito: "))
        
        if deposito > 0: 
            saldo += deposito
            extrato += f"{ data}\n Depósito: R$ {deposito:.2f}\n\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        saque = float(input("Digite o valor para saque: "))

        saldo_excedido = saque > saldo
        limite_excedido = saque > limite
        saques_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print('Operação inválida! Saldo insuficiente')
        elif limite_excedido:
            print('Operação inválida! Limite insuficiente')
        elif saques_excedido:
            print('Operação inválida! Limites de saques diário atingido')

        elif saque > 0 :
            saldo -= saque
            extrato += f"{data}\n Saque: R$ {saque:.2f} \n\n"
            numero_saques += 1

        else:
            print('Operação inválida! Valor informado é inválido')

    elif opcao == "e":
        print("\n########## EXTRATO ##########")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("####################################")
    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")