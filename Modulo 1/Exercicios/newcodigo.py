#crie um codigo python utilizando match case que analise as notas dos alunos:
#1) peça ao usuario 4 notas
#2) calcule a média
#3) classifique a média em:
# 0 a 4=reprovado
#5 e 6= recuperação
#7 a 10 = aprovado

nota1=int(input("digite sua nota"))
nota2=int(input("digite sua nota"))
nota3=int(input("digite sua nota"))
nota4=int(input("digite sua nota"))
          
# 2) calculo da media

media=(nota1+ nota2+ nota3+ nota4) /4

# 3) condicional

match media:
    case media if media <5:
        print(f"sua media foi {media:.2f} e esta reprovado")
    case media if 5 <= media <7:
        print(f"sua media foi {media:.2f} e esta reprovado")
    case media if 7 <= media <=10:
        print(f"sua media foi {media:.2f} e esta aprovado")
    case _:
        print(f"nota invalida, verifique as informaçoes")