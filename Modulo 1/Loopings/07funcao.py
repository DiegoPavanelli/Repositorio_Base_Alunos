
def calcular_bebida(convidados,consumo_por_pessoa_ml=800, volume_garrafa_litros=2.25):
    total_ml = convidados * consumo_por_pessoa_ml
    total_litros = total_ml/1000

    garrafas = int(total_litros//volume_garrafa_litros)
    if total_litros %volume_garrafa_litros > 0:
        garrafas +=1
    return total_litros, garrafas

def calcular_carnes(convidados,consumo_por_pessoa_gramas=400):
    total_gramas = convidados * consumo_por_pessoa_gramas
    total_kg = total_gramas /1000
    return total_kg

convidados = int(input("digite o numero de convidados:"))

litros, garrafas = calcular_bebida(convidados)
carne_kg = calcular_carnes(convidados)

print("n\=== quantidade total para churrasco ===")
print(f"numero de convidados:{convidados}")
print(f"refrigerante necessario:{litros:.2f} litros")
print(f"Garrafas de 2,25L: {garrafas} unidades")
print(f"Carne necessaria: {carne_kg:.2f} kg ")

