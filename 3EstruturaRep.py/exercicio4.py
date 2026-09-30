# Peça o valor de 5 produtos digitados pelo usuario e mostre
# o valor total da compra e a media dos valores digitados

soma = 0 
for valor in range(1,6):
    somas = float(input("Valor do produto" + str(valor) + ":"))
    soma = soma + somas 
    media = soma/valor
print("valor total = ", soma, "e media = ",media)