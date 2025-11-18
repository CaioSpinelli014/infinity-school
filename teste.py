hora = float(input("Quanto você ganha por hora?: "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês?: "))


salario_bruto = hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f"Salário Bruto = R${salario_bruto:.2f}")
print(f"ir = R${ir:.2f}")
print(f"Inss = R${inss:.2f}")
print(f"sindicato = R${sindicato:.2f}")
print(f"Salário Liquido = R${salario_liquido:.2f}")

# Solicitar o número de alunos
numero_alunos = int(input("Informe o número de alunos: "))

# Inicializar variáveis para armazenar a soma das médias e os dados dos alunos
soma_medias = 0

