# Peça ao usuario um numero inteiro e mostre todos os numeros pares ate esse valor
inteiro = int(input("Digite um numero positivo e inteiro: "))
for numero in range(2,inteiro+1):
    if inteiro %2 ==0:
        print(numero)
