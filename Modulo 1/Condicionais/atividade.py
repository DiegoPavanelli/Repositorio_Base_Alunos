def ler_notas():
    """Lê três notas do usuário e retorna como uma lista."""
    return [float(input(f"Digite a {i}ª nota: ")) for i in range(1, 4)]
def calcular_media(notas):
    """Calcula e retorna a média das notas fornecidas."""
    return sum(notas) / len(notas)
def situacao_aluno(media):
    """Determina a situação do aluno com base na média."""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Em recuperação"
    return "Reprovado"
def main():
    """Função principal que executa o programa."""
    notas = ler_notas()  # Lê as notas do usuário
    media = calcular_media(notas)  # Calcula a média
    print(f"Média: {media:.2f}")  # Exibe a média
    print(f"Situação do aluno: {situacao_aluno(media)}")  # Exibe a situação
if __name__ == "__main__":
    main()
