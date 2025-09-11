
#programa infraçoes de transito: rodizio e velocidade

#1 pergunte se e rdizio do carro
rodizio = input("hoje é rodizio do carro? (sim/não):").strip().lower()
#2 pergunte a vlocidade do carro
velocidade = float(input ("qual a velocidade atual do veiculo (Km/h)? "))

#3 defina a velocidade da via 
limitevia = 60

#4 verifique as infraçoes
if rodizio == "sim" and velocidade > limitevia:
    print("voce esta dirigndo no seu dia de rodizio e acima da velocidade permitida")
    print("voce sera autuado por ambas as infrações.")
elif rodizio == "sim": 
    print("voce esta dirigindo no seu dia de rodizio e sera autuado por isso")
elif velocidade > limitevia:
    print("voce esta dirigindo acima da velocidade permitida e sera autuado por excesso de velocidade")
else:
    print("tudo certo voce esta dentro da lei dirija com seguraça")
            