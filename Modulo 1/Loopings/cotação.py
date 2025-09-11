# Taxa de câmbio (exemplo)
taxa_cambio = 5.25  # 1 USD = 5.25 BRL
# perguntando ao usuario qual troca 
while True:
    print("Escolha a conversão:")
    print("1: Real para Dólar")
    print("2: Dólar para Real")
    print("3: Sair")
    
    escolha = input("Digite sua escolha (1/2/3): ")
    #calculo cambio 1
    if escolha == '1':
        valor_real = float(input("Digite o valor em Reais: "))
        valor_dolar = valor_real / taxa_cambio
        print(f"{valor_real} BRL é igual a {valor_dolar:.2f} USD")
    #calculo cambio 2
    elif escolha == '2':
        valor_dolar = float(input("Digite o valor em Dólares: "))
        valor_real = valor_dolar * taxa_cambio
        print(f"{valor_dolar} USD é igual a {valor_real:.2f} BRL")
    #sair do cambio
    elif escolha == '3':
        print("Saindo...")
    #erro 
    else:
        print("Escolha inválida. Tente novamente.")
