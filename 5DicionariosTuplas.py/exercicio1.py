valorNovo = float(input("Digite o valor: "))
id = int(input("Digite o id: "))

sensor = {"id":id,
          "tipo":"Temperatura",
          "valor":valorNovo,
          "unidade": "C°"
          }   

def exibirInformacoes(sensor):
    for titulo,valor in sensor.items():
     print(titulo,":",valor)

def alerta(sensor):
    if sensor["valor"] > 37:
     print("ATENÇAO\n")
    else:
     print("NORMAL\n")

exibirInformacoes(sensor)
alerta(sensor)