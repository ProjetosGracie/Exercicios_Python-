nome = input("Informe seu nome: ").split()
temperatura = float(input("Informe a Temperatura: "))
bateria = float(input("Informe a bateria: "))
observacao = input("Informe a Observacao: ")

with open("DiarioMissao.txt","w") as arquivo:
    arquivo.write(f"Operador: {nome}\n")
    arquivo.write(f"Temperatura: {str(temperatura)}\n")
    arquivo.write(f"Bateria: {str(bateria)}\n")
    arquivo.write(f"Operador: {observacao}\n")