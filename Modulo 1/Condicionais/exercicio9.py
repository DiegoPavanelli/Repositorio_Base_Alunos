valor_compra= float(input("digite o valor da compra RS: "))

if valor_compra >= 150:
    valor_final= valor_compra - 20
    print(f" obrigada pela sua compra, o valor a pagar RS {valor_final:.2f}.")
else:
    print(f"obrigada pela compra, valor final RS {valor_compra:.2f}.")