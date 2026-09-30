# Divisao com Segurança
try:
    numero1 = float(input("Digite um numero : "))
    numero2 = float(input("Digite outro numero : "))
    divisao = numero1/numero2
    print("Divisao: ",divisao)

except ValueError:
    print("Digite um numero animal, imbecil")
except ZeroDivisionError:
    print("O segundo numero é o divisor, nao pode ser zero")
except:
    print("Erro do programado")


