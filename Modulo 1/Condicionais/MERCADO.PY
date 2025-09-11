estoque = {}

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    estoque[nome] = estoque.get(nome, 0) + quantidade
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    if not estoque:
        print("Não há produtos no estoque.")
    else:
        print("Produtos em estoque:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")
def vender_produto():
    nome = input("Digite o nome do produto que deseja vender: ")
    if nome in estoque:
        quantidade_venda = int(input("Digite a quantidade a ser vendida: "))
        if quantidade_venda <= estoque[nome]:
            estoque[nome] -= quantidade_venda
            print(f"Venda de {quantidade_venda} unidades de '{nome}' realizada com sucesso!")
            if estoque[nome] == 0:
                del estoque[nome]
        else:
            print("Quantidade em estoque insuficiente.")
    else:
        print("Produto não encontrado no estoque.")

def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Vender produto")
    print("4. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            vender_produto()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
