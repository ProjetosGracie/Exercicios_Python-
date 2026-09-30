# Calcule o total gasto com livros e canetas
L = int(input('Quantos livros voce comrpou: '))
C = int(input('Quantas canetas voce comprou: '))
LP = float(input('Qual o preço do livro: '))
CP = float(input('Qual o preço da caneta: '))
total = (L * LP) + (C * CP)
print(f'O calor que voce gastou foi de {total:.2f}')