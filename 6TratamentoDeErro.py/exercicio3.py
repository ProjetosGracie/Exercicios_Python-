# Cadastro de idade
try:
    idade = int(input("Digite sua idade: "))

except ValueError:
    print("DIgita um numero")

else:
    if 0 < idade <=120:
        print("IDADE CADASTRADA")
    else:
        print("Intervalo permitido entre 1 a 120 anos")

finally:
    print("Tentativa de cadastro encerrada")