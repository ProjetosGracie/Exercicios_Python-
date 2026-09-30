# Faça um menmu de Lanchonete
lachonete = input("Digite 1 - X-Burguer: \n Digite 2 - Batata Frita: \n Digite 3 - Refrigerante: \n Digite 4 - Encerramento: ")
while lachonete:
    if lachonete == '1':
     print("Pediu X-Burguer")
    elif lachonete == '2':
     print("Pediu batata frita")
    elif lachonete == '3':
     print("Pediu refri")
    elif lachonete == '4':
     print("encerrou ")
     break
    else:
     print('opcao invalidade')
     
    lachonete = input("\nDigite outra opção: " )