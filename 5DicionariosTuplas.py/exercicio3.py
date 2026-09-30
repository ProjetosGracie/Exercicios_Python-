produto = {
   "codigo":546,
   "nome":"nome",
   "preco":54,
   "estoque":4
}

for titulo,valor in produto.items():
  print(titulo,"-",valor)
  produto["estoque"] =  produto["estoque"] - 1

for titulo,valor in produto.items():
  print(titulo,"-",valor)