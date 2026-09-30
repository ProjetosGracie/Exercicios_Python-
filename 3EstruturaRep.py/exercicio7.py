# Caixa eletronico simples 
saldo = 1000
caixa_eletronico = int(input("1 - Consultar Saldo  \n 2 - Depositar Saldo \n 3 - Sacar Valor  \n 4 - Sair\n Qual numero: "))
while caixa_eletronico:

    if caixa_eletronico == 1:
        print(saldo)

    elif caixa_eletronico == 2:
        deposito = float(input("Digite o saldo que deseja depositar: "))
        print("Seu atual saldo é R$",deposito + saldo)

    elif caixa_eletronico == 3:
        sacar = float(input("Digite o saldo que deseja sacar: "))
        if sacar<=saldo:
         print("Seu atual saldo é R$",saldo - sacar)
        else:
            print("Saldo Insuficiente")

    elif caixa_eletronico == 4:
        print("Sistema encerrado")
        break 
    else:
        print("Opçao invalida")
        
    caixa_eletronico = int(input("1 - Consultar Saldo  \n 2 - Depositar Saldo \n 3 - Sacar Valor  \n 4 - Sair\n Qual numero: "))

    