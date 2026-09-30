# Cardapio em amtriz
cardapio = [["X-Burguer",30],
           ["Batata Frita", 20],
           ["Suco", 10]]

print("0 -",cardapio[0][0],"-R$",cardapio[0][1])
print("1 -",cardapio[1][0],"-R$",cardapio[1][1])
print("2 -",cardapio[2][0],"-R$",cardapio[2][1])

opcao = int(input("Digite a opcao desejada: "))
qntd = int(input("Digite quantidade desejada: "))

produto = cardapio[opcao][0]
preco = cardapio[opcao][1]
total = preco * qntd

print("Produto escolhido:", produto)
print("Quantidade:", qntd)
print("Total: R$", total)