# leia dois valores A e B, que correspondaem a 2 notas de um aluno.
# Calcule e informe a media ponderada do aluno

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))            
p1 = int(input('Digite o peso da primeira nota: '))
p2 = int(input('Digite o peso da segunda nota: '))
m = (n1*p1 + n2*p2) / (p1 + p2)