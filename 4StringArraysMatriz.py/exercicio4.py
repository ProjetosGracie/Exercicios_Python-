# Cadastro de participantes
nome = []
quantidade_grandes = 0

for i in range(1,6):
    nomes = input("Digite o nome " + str(i) + ": ")
    nome.append(nomes)
    
for i in range(0,len(nome)):
    print(i , "-", nome[i])

for nomes in nome:
    if len(nome)>5:
     quantidade_grandes = quantidade_grandes + 1

print("Quantidade de nomes com mais de 5 letras:", quantidade_grandes)
