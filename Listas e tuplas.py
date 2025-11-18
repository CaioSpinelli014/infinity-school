# LISTAS
fruta = ["banana", "laranja","melancia", "kiwi", "maçã", "Tomate"]

tupla_f = tuple(fruta)

print(tupla_f)

lista_de_compras = [
    "quijo",
    "feijão",
    "arroz",
    "macarrão",
    "laranja"
]


lista_de_compras.append("legumes") # adiconar um item ao final da lista
lista_de_compras.append("Gosto de café") # adiciona um item ao final da lista
lista_de_compras.insert(2, "manga") # adciona um item na posição informada
lista_de_compras.insert(3, "queijo ralado") # adiciona um item na posição informada
lista_de_compras.insert(5, "frango") #adiciona um item na posição ionformada
lista_de_compras.pop(0) # remove um item atraves de seu índice
lista_de_compras.remove("macarrão")# remove um item atraves de seu valor


print("LISTA DE COMPRAS", end='\n\n')

for itens in lista_de_compras:
    print("[ ]", itens)
#
################################################################################
# TUPLAS
frutas = ("maçã", "banana", "laranja", "abacaxi")

indice_laranja = frutas.index("laranja")
print("Indice laranja =", indice_laranja)

indice_abacaxi = frutas.index("abacaxi")
print("indice_abacaxi =", indice_abacaxi)

indice_banana = frutas.count("banana")
print("Quantidades de bananas =", indice_banana)

