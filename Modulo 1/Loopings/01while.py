letra = "s"
while letra == "s":
    n1 = float(input('Digite a PRIMEIRA nota:'))
    n2 = float(input('Digite a SEGGUNDA nota:'))
    n3 = float(input('Digite a TERCEIRA nota:'))

    soma = n1 + n2 + n3
    media = soma / 3

print(f"a media do alumo e :{round(media,2)}")
if media >= 7:
    print("aprovado")
elif media >3:
    print("recuperação")
else:
    print("reprovado")
     
letra = input("deseja continuar? (S/N):")

############################################################

letra = "s"
while letra == "s":
    n1 = float(input('Digite um numero:'))
    n2 = float(input('Digite a porcentagem que deseja descobrir:'))

    porcentagem = (n1*n2)/100
    print(f'a porcentagem é igual a: {porcentagem}:')
    letra = input("deseja continuar? (s/m):")


##############################################################













