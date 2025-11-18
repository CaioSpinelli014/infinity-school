frutas = set([])

frutas_1 = {"maçã", "banana", "uva", "laranja", "morango"}

frutas.update(frutas_1)
print(frutas)

print(frutas.intersection("Banana"))

frutas_vermelhas = {"morango", "cereja", "framboesa"}

print(frutas_vermelhas)

print(frutas_vermelhas.remove("cereja"))
print(frutas_vermelhas)
#################################################################
carro = {"fiat", "ford", "ferrari"}
moto = {"pop100", "gt1000", "yamara"}

print(carro.union(moto))
######################################################################
nome_1 = [1, 2, 3, 4]

dados = {
    "Nome" : "Caio",
    "idade" : 20,
    "cidade" : "Recife"
}
for chave,valor in dados.items():
    print(f"Ola {chave}, {valor}")
#################################################################
dicionario = {}
lista = []

lista = input("Digite uma lista: ")
dicionario = input("Digite um dicionario: ")

print(lista in dicionario)

contato = {}

for _ in range(1):
    contato["nome"] = []
    contato["telefone"] = []
    contato["email"] = []
    for _ in range(1):
        name = input("Digite seu nome: ")
        fone = input("Digite seu telefone: ")
        g_mail = input("Digite seu E-mail: ")
        contato["nome"].append(name)
        contato["telefone"].append(fone)
        contato["email"].append(g_mail)

for chave, valor in contato.items():
     print(f"{chave}, {valor}")

 alunos = {}


 for i in range(3):
     nome = input(f"Digite o nome do {i + 1}º aluno: ")
     alunos[nome] = []
     nota_list = []
     for j in range(3):
         notas = input(f"Digite a nota {j+1} de matematica: ")
         nota_list.append(notas)
     alunos[nome].append(nota_list)

 for chave, valor in alunos.items():
     print(f"{chave}, {valor}")




