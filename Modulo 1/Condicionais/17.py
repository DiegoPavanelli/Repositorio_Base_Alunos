def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

def obter_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calcular():
    print("Calculadora com Tratamento de Erros")
    print("Operações disponíveis:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Escolha uma operação (1/2/3/4): ")

    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida.")
        return

    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")

    if operacao == '1':
        resultado = adicionar(num1, num2)
        operador = '+'
    elif operacao == '2':
        resultado = subtrair(num1, num2)
        operador = '-'
    elif operacao == '3':
        resultado = multiplicar(num1, num2)
        operador = '*'
    else:  # operação == '4'
        resultado = dividir(num1, num2)
        operador = '/'

    print(f"{num1} {operador} {num2} = {resultado}")

# Executa a calculadora
calcular()
