contador = 0

while True:
 contador += 1
 
 print(f"--------- {contador}° REGISTRO NOVO -----------")
 print("--------- (lembradno que tudo vai ser em porcentagem) ---------")
 sensor = input("Informe o sensor: ").upper()
 valor = float(input("Informe o valor: "))

 if 50 <= valor < 75:
   status = "ATENCAO"
 elif valor >= 75:
   status = "NORMAL"
 else:
   status = "CRITICO"

 with open("Alertas.txt","a") as arquivo:
    arquivo.write(f"{sensor}|{str(valor)}%|{status}\n")

 terminar = input("Deseja informar mais algum sensor(S/N): ").upper()
 if terminar == "N":
   print("Quantidade de registros Cadastrados: ",contador)
   break