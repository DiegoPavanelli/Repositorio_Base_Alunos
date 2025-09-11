
n= int(input("Digite um numero para saber o fatorial: "))
resultado =1
f= 1

while f <= n:
    resultado *= f
    f += 1
    print(f"o fatorial do {n} é : , {resultado}")
