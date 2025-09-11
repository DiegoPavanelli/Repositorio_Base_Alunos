# Programa para salvar informações de produtos no arquivo produtos.txt
def salvar_produto(nome, valor, quantidade):
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Produto: {nome}, Valor: {valor}, Quantidade: {quantidade}\n")

def main():
    print("Cadastro de Produtos")
    nome = input("Digite o nome do produto: ")
    
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            break
        except ValueError:
            print("Quantidade inválida. Por favor, digite um número inteiro.")
    
    salvar_produto(nome, valor, quantidade)
    print("Produto salvo com sucesso no arquivo produtos.txt")

if __name__ == "__main__":
    main()
