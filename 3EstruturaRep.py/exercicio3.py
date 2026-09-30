# Faça uma tabuada de acordo com o que o usuario pede
tabuada = int(input("Digite um número: "))
for numero in range(1,11):
    print(f'{tabuada}x{numero}={tabuada*numero}' )