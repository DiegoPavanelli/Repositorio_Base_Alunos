# Programa para salvar nome e e-mail em um arquivo contatos.txt

def salvar_contato(nome, email):
    with open("contatos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}, Email: {email}\n")

def main():
    print("Cadastro de Contatos")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    salvar_contato(nome, email)
    print("Contato salvo com sucesso no arquivo contatos.txt")

if __name__ == "__main__":
    main()

