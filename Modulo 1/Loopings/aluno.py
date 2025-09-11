
nome = input("Digite o nome do aluno: ")
notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]
media = sum(notas) / 3
print(f"{media:.2f}")

