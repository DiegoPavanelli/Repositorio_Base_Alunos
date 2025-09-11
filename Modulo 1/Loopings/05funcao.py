def calcular_volume_cm3(altura, largura, profundidade):
    return altura * largura * profundidade

altura = float(input("Digite a altura em (cm):"))
largura = float(input("digite a largura em (cm):"))
profundidade= float(input("Digite a profundidade em (cm):"))

volume_cm3 = calcular_volume_cm3(altura, largura, profundidade)
print(f"\nas medidas do aquario são:")
print(f"altura: {altura} cm")
print(f"largura: {largura} cm")
print(f"profundidade: {profundidade} cm")
print(f"protanto,seu volume é {volume_cm3:.2f} cm3 ({volume_cm3 / 1000:.2f} litros).")