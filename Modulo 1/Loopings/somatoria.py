#prova01 Diego pavanelli
# calculadora de imc
# coletar dados 
nome =input("digite seu nome: ")
peso = float(input("digite seu peso kg: "))
altura = float(input("digite sua altura: "))
#calcular o imc do paciente
imc = peso / (altura ** 2)
# Exibição do IMC
print(f"\n{nome}, seu IMC e: {imc:.2f}")
#texto para o paciente
if imc >= 30.0:
        print("cuidado com a saude")
else:
       print("tudo ok")
#tipos de pesos
if imc < 18.5:
   classificacao = "abaixo do peso"
elif 18.5 <= imc < 25.0:
   classificacao = "peso normal"
elif 25.0 <= imc < 30.0:
   classificacao = "sobrepeso"
elif 30.0 <= imc < 35.0:
   classificacao = "obesidade grau 1"
elif 35.0 <= imc < 40.0:
   classificacao = "obesidade grau 2"
else:
   classificacao = "obesidade grau 3 morbida"
# classificação do paciente
print(f"Classificação: c")
