# Solicita peso (kg) e altura (m)
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
# Calcula IMC
imc = peso / (altura ** 2)
# Exibe o IMC com duas casas decimais
print(f"Seu IMC é {imc:.2f}")
# Classificação conforme OMS
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III (mórbida)"
# Exibe a classificação
print(f"Classificação: {classificacao}")
