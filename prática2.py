# Solicitar o número de alunos
numero_alunos = int(input("Informe o número de alunos: "))

# Inicializar variáveis para armazenar a soma das médias e os dados dos alunos
soma_medias = 0

# Loop para obter os dados de cada aluno
for i in range(numero_alunos):
    nome = input(f"Informe o nome do aluno {i + 1}: ")
    nota1 = float(input(f"Informe a primeira nota de {nome}: "))
    nota2 = float(input(f"Informe a segunda nota de {nome}: "))
    nota3 = float(input(f"Informe a terceira nota de {nome}: "))

    # Calcular a média das notas
    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    # Verificar se o aluno foi aprovado ou reprovado
    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    # Exibir os dados do aluno
    print(f"\nAluno: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}\n")

# Calcular e exibir a média geral da turma
media_geral = soma_medias / numero_alunos
print(f"Média geral da turma: {media_geral:.2f}")