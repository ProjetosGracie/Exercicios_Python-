# Mochila de Explorador 
mochila = ["Garrafa", "Lanterna","Mapa", "Cassaco"]
print("Mochila Inicial")
print(mochila)

novo = input("Digite um item para colocar na mochila: ")
mochila.append(novo)
print("Mochila com novo item")
print(mochila)

remover = int(input("Digite o numero da posição que voce quer remover: "))
mochila.pop(remover)
print("Mochila com item removido")
print(mochila)