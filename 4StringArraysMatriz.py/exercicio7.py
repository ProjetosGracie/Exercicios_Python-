# Boletim da turma 
nomes = []
notas = []
for i in range(1,4):
    nome = input("Digite o seu nome("+str(i)+" pessoa)")
    nomes.append(nome)
    lista_notas = []
    
    for j in range(1,3):
        nota = float(input("Digite a sua "+ str(j) +" nota "+nome))
        lista_notas.append(nota)
    notas.append(lista_notas)

print("BOLETIM")
for i in range(0,len(nomes)):
    soma = 0
    for nota in notas[i]:
        soma = soma + nota
    media = soma/len(notas[i])

    print("Aluno:", nomes[i])
    print("Notas:", notas[i])
    print("Média:", media)
    if media >= 6:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")
