# Nota valida com nova tentativa
while True:
 try:
    nota = float(input("Digite a nota que deseja: "))

 except ValueError:
   print("Digite um numero que esteja de acordo com a nota")

 else:
    if 0<=nota <=10:
      print("Intervalo aceito ")
      break
    else:
      print("Digite entre 0 a 10")


if nota >=6:
 print("APROVADO")
else:
  print("Reprovado")
   