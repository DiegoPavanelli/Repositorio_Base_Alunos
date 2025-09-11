turno= input("Qual e o seu turno de trabalho (M= manha ou T= tarde)?"). strip().upper()

if turno == "M":
    print("Voce trabalha no turno da manha")
elif turno == "T":
    print ("Voce trabalha no turno da tarde")
else:
    print("Voce digitou um turno invalido. Digite um turno valido")