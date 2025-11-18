inicio = int(input("Digite um número inteiros: "))
fim = int(input("Digite um número inteiros: "))
soma = 0

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i

if soma != 0:
    print(soma)
else:
    print("Não há números pares!")


