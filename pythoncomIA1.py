lista_de_numeros = [1,2,3,4,5]
lista_de_vogais = ['a', 'e', 'i', 'o', 'u']

print(lista_de_numeros)
print(lista_de_vogais)

lista_estranha = [1, "a", 2.3, True, "oi"]

print(lista_estranha[2])

lista = []
variavel = "g.a"
lista.append(variavel)
print(lista)

lista1_2 = ['meia', 'calça', 'blusa']
lista1_2.insert(2, 'short')
lista1_2.remove('short')
lista1_2
print(lista1_2)

palestrante = (
    ("Caio Afonso", "python_IA", "Fiap"),
    ("Aline", "Git_hub", "Infinity"),
    ("Victor", "Linkedin", "Espaço_ciencia")

)
print(f"informações do terceiro palestrante: {palestrante[2]}")
equipe1 = ("raio de sol", [10, 8, 7, 8])
equipe2 = ("Lua noturna", [9, 6, 7, 9])
equipe3 = ("Galo sego", [8, 6, 4, 5])

competicao = [equipe1, equipe2, equipe3]

for equipe in competicao:

