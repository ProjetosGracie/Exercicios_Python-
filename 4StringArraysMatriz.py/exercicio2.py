# Lista de Filmes favoritos
filme = []
for i in range(1,6):
    filmes = input("Digite o seu "+str(i)+ ": ")
    filme.append(filmes)

for i in range(0, len(filme)):
    print(i, "-", filme[i]) 