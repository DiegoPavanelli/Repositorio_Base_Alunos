def obter_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

# Chama a função para obter um número do usuário
numero_usuario = obter_numero()
print(f"O número digitado foi: {numero_usuario}")
