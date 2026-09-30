# Dobro o numero
try:
    numero = int(input("Digite um numero inteiro: "))
    dobro = numero*2
    print("Dobro: ",dobro)
except ValueError:
    print("informe um numero inteiro")
except:
    print("erro no programador")


