# Solicita o número para a tabuada
numero = int(input("Digite um número para ver a tabuada: "))

# Gera a tabuada usando um laço for de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
