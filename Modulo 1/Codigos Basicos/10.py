# Inicializa soma
soma = 0
# Solicita 5 números ao usuário
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    soma += num
# Calcula a média
media = soma / 5
# Exibe a média com duas casas decimais
print(f"A média dos números digitados é: {media:.2f}")
