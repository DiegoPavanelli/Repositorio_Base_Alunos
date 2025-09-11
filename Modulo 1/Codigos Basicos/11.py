# Inicializa uma lista vazia
nomes = []
# Solicita 5 nomes ao usuário
for i in range(1, 6):
    nome = input(f"Digite o nome {i}: ")
    nomes.append(nome)
# Exibe os nomes um por um
print("Nomes digitados:")
for nome in nomes:
    print(nome)
