nomeArquivo = input("Informe o nome do arquivo que deseja ver: ")
print()

def ler(nomeArquivo):
 try:
    with open(nomeArquivo,"r") as arquivo:
     for linha in arquivo:
      print(linha.strip())
 except FileNotFoundError:
  print("Arquivo nao existe")

ler(nomeArquivo)

# se quiser colocar em uma lista coloque split(",") no final do print(linha.strip())