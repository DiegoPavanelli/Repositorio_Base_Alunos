
#crie um programa que pergunte ao cliente se é sua primeira compra
#depois pergunte o valor total da compra
#se for a primeira compra do usuario e esta for maior que 500 r$
#inoforme que ele ganhou um brinde e imprima uma mensagem de boas vindas 
#caso contrario imprima uma mensagem de agradecimento 

#etapas 
#1) pergunte ao usuario se é a primeira compra dele
primeiracompra = input ("é usa primeira compra conosco? (sim/não):").strip().lower()
#2) pergunte ao usuario o total da compra 
valorcompra = float (input ("Informe o valor total da sua compra: R$"))
#3) verifique a condiçao para o brinde 
if primeiracompra == "sim" and valorcompra > 500:
    print ("Parabéns ! Seja bem vindo (a), voce ganhou um brinde")
else: 
    print ("Obrigado pela sua compra! volte sempre!")
#4) informe se o usuario ganhou ou não o brinde 

