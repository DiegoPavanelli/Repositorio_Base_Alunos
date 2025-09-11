
print("revisão For")
# o for executa um bloco varias vezes
frutas = ["maça", "banana", "abacate", "caju", "melancia", "morango"]

for fruta in frutas:
    print(f"eu gosto de {fruta}")

carros = ["polo", "fit", "pegeout", "bmw", "ford", "punto", "civic", "toyota"]

for carro in carros:
    print(f"vou comprar um {carro}")

#while executa um bloco 'enquanto' (while) um condição for verdadeira

contador = 1 
while contador <= 5:
    print (f"contador:{contador}")
    contador = contador + 1

print("sair do while... ufa !!!")

#Crie um  programa quer peça a senha do cliente. a senha precisa ser senha 135
#se a senha estiver correta, imprima esta ok caso contrario informe tambem 

senha_cadastrada = 'senha135'
senha = input('digite sua senha:')
if  senha == senha_cadastrada:
   print('esta ok')
else:
    print("senha incorreta")

#desf2

senha = ""
while senha != "senha135":
    senha 

