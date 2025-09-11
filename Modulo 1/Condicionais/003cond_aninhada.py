# Classificação por idade
# Faça um programa que leia a idade de uma pessoa e classifique-a em :
# criança : menor que 12 anos
# adolescente : entre 12 e 17 anos
# adulto: maior ou igual a 18 anos
# utilize a estrutura de condicional aninhada

idade= int(input("qual é a sua idade "))
if idade>0:
    if idade>= 18:
        print(f"voce tem {idade} anos e é um adulto")
    elif 12 <=idade <=17:
        print(f'voce tem {idade} e é um adolescente. ')
    else:
         print(f'voce tem {idade} e é uma criança. ')
else:
    print(" idade nao podeser negativa, digite uma idade valida.")
