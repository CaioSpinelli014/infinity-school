print("Bem vindo ao celular, apos aplicar a nova senha irá pedir para conferir")
senha_loguin = float(input("Digite a sua nova senha: "))

tentativas = 0

for i in range(3, 0, -1):
    senha = float(input("senha: "))
    if senha != senha_loguin:
        print(f"senha incorreta, Você tem {i - 1} tentativas até o bloqueio!")
    else:
        print("bem vindo")
        break