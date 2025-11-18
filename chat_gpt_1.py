#  Solicita uma palavra do usuário
# palavra = input("Digite uma palavra: ")
#
# Inicializa uma string para armazenar as vogais
# vogais_somente = ""
#
#  Itera sobre cada caractere da palavra
# for caractere in palavra:
#     # Verifica se o caractere é uma vogal
#     if caractere in 'aeiouAEIOU':
#         vogais_somente += caractere
#
#  Exibe somente as vogais da palavra
# print(f"As vogais na palavra são: {vogais_somente}")

numero = []

if i in range(5):
    num = int(input(f"Digite {i+1} numeros:"))
    numero.append(num)

maior = numero[0]

for num in numero:
    if num > numero:
        maior = num

print(f"O maior número é: {maior}")


