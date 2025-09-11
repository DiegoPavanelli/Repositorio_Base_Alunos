conta= float(input("Digite o valor da conta R$: "))

if conta >= 100:
    conta_final= conta +(conta *0.1)
    print(f' Obrigada por sua visita, sua conta e R$ {conta_final:.2f}.')
else: 
    #conta_final = conta +(conta*0.05)
    conta_final= conta*1.05
    print(f' Obrigada por sua visita, sua conta e R$ {conta_final:.2f}.')