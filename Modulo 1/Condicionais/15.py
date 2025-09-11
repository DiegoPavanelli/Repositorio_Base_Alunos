def fatorial(n):
    """Calcula o fatorial de um número n."""
    if n < 0:
        return "Fatorial não definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Exemplo de uso da função
numero = int(input("Digite um número inteiro não negativo: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
