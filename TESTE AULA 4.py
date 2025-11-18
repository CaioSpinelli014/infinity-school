cont = "ok"

while cont != "pare":
    soma = float(input("número 1: "))
    soma2 = float(input("Númmero 2: "))
    soma_geral = soma + soma2
    print(f"Sua soma deu: {soma_geral.__round__()}")
    cont = input("Se quer fazer outra soma digite 'ok' se quer parar 'pare': ")

print("Muito obrigado por usar o some.aqui")

contador = 0

while contador < 50:
    if contador % 2 != 0:
        print(contador)

    contador += 1



