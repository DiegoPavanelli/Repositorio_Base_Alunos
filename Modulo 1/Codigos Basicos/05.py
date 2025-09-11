# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# Calcula a média
media = (nota1 + nota2 + nota3) / 3
# Exibe a média com duas casas decimais
print(f"Média: {media:.2f}")
# Avalia a situação do aluno
if media >= 7:
    print("Aluno aprovado.")
elif 4 < media < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
