# Vendas de Vendedores
vendas = []
for vendedor in range(1,4):
    linha = []
    print("Vendedor", vendedor)
    for i in range(1,4):
        valor = float(input("Digite o valor do" +str(i),"dia: "))
        linha.append(valor)
    vendas.append(linha)
print()
for i in range(0,len(vendas)):
    total = 0
    for valor in vendas[i]:
        total = total + valor

print("Vendedor ",i + 1,"-", "Total Vendido: R$", total )