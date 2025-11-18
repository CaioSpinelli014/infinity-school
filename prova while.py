contador = 0
num = 0

while contador != 3:
    num = int(input("Digite um número aleatório entre 1 e 10, e tente acerta o número secreto, você só tem 3 tentativas: "))
    if num == 5:
        contador = 2
    else:
        print("Você consegue, tente mais uma vez!")

    contador += 1

if num != 5:
    print("É uma pena, VOCÊ não conseguiu, tente novamente!")
else:
    print("PARABÉNS você conseguiu acerta o número secreto!!")

