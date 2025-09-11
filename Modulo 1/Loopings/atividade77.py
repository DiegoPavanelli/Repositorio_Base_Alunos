
def calcular_preco_final(valor_compra):
    if valor_compra < 100:
        desconto = 0
    elif 100 <= valor_compra <= 500:
        desconto = 0.05  
    else:
        desconto = 0.10 
        
    preco_final = valor_compra * (1 - desconto)
    return preco_final

valor = float(input("Digite o valor total da compra: R$ "))
preco_final = calcular_preco_final(valor)
print(f"O preço final após o desconto é: R$ {preco_final:.2f}")

