from random import randrange
from click import clear

def exibir_tabuleiro(tabuleiro):
    clear()
    print("+-------"*3, "+", sep="")
    for linha in range(3):
        print("|       "*3,"|", sep="" )
        for coluna in range(3):
            print("|   "+str(tabuleiro[linha][coluna])+"   ", end="")
        print("|")
        print("|       "*3, "|", sep="")
        print("+-------"*3, "+",sep="")

def entrada_jogador(tabuleiro):
    valido = False
    while not valido:
        movimento = input("Digite seu movimento: ")            
        valido = len(movimento) == 1 and movimento >= "1" and movimento <= "9"
        if not valido:
            print("Movimento ruim - repita sua entrada!")
            continue
        movimento = int(movimento) - 1
        linha = movimento // 3
        coluna = movimento % 3
        conteudo = tabuleiro[linha][coluna]
        valido = conteudo not in ["o", "x"]
        if not valido:
            print("Campo ja ocupado - repita sua entrada!")
            continue
        tabuleiro[linha][coluna] ="o"

def lista_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ["O","X"]:
                livres.append((linha, coluna))
    return livres

def verifica_vitoria(tabuleiro, sinal):
    if sinal == "X":
        vencedor = "computador"
    elif sinal == "O":
        vencedor = "jogador"
    else:
        vencedor = None

    diag1 = diag2 = True
    for i in range(3):
        if tabuleiro[i][0] == sinal and tabuleiro[i][1] == sinal and tabuleiro[i][2] == sinal:
            return vencedor
        if tabuleiro[0][i] == sinal and tabuleiro[1][i] == sinal  and tabuleiro[2][i] == sinal:
            return vencedor
        if tabuleiro[i][i] != sinal:
            diag1 = False
        if tabuleiro[i][2 - i] != sinal:
            diag2 = False
    if diag1 or diag2:
        return vencedor
    return None

def jogada_computador(tabuleiro):
    livres = lista_campos_livres(tabuleiro)
    quantidade = len(livres)
    if quantidade > 0:
        escolha = randrange(quantidade)
        linha, coluna = livres[escolha]
        tabuleiro[linha][coluna] = "x"

tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = "x"
livres = lista_campos_livres(tabuleiro)
vez_jogador = True 
vencedor = None

while len(livres) and vencedor is None:
    exibir_tabuleiro(tabuleiro)
    if vez_jogador:
        entrada_jogador(tabuleiro)
        vencedor = verifica_vitoria(tabuleiro, "o")
    else:
        jogada_computador(tabuleiro)
        vencedor = verifica_vitoria(tabuleiro, "o")
    vez_jogador = not vez_jogador
    livres = lista_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == "jogador":
    print("voce ganhou!")
elif vencedor == "computador":
    print("eu venci!")
else:
    print("empate!")

