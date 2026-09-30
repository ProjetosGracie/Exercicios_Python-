# Senha com limite de tentativas
senha_correta = "1234"
tentativas = 0
acertou = False

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado")
        acertou = True
        break
    tentativas = tentativas + 1
    print("Senha incorreta")
if acertou == False:
    print("Conta bloqueada")