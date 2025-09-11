def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def calcular():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Escolha uma operação (1/2/3/4): ")

    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida.")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        return

    if operacao == '1':
        resultado = adicionar(num1, num2)
        operador = '+'
    elif operacao == '2':
        resultado = subtrair(num1, num2)
        operador = '-'
    elif operacao == '3':
        resultado = multiplicar(num1, num2)
        operador = '*'
    else:
        resultado = dividir(num1, num2)
        operador = '/'

    print(f"{num1} {operador} {num2} = {resultado}")

# Executa a calculadora
calcular()
