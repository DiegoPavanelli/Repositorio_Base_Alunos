# Solicita o número do usuário
numero = int(input("Digite um número inteiro: "))

print(f"Divisores de {numero}:")

# Verifica todos os números de 1 até o número informado
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
