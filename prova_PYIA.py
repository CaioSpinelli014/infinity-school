produtos = {}

for i in range(5):
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input(f"Digite o preço do produto {nome_produto}: "))

    produtos[nome_produto] = preco_produto

valor_total = sum(produtos.values())

print(f"O valor total da compra é: R$ {valor_total:.2f}")