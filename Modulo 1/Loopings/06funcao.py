# Função para calcular o volume em litros (1 m3 = 1000 litros) 

def calcular_volume_m3(comprimento, largura, profundidade):
 return comprimento * largura * profundidade
# Função para calcular o volume restante 

def volume_restante(volume_total_litros, volume_retirado_litros):
 return volume_total_litros - volume_retirado_litros
# Solicitação das dimensões

comprimento = float(input("Digite comprimento em (m): "))
largura = float(input ("Digite a largura em (m): "))
profundidade = float(input("Digite a profundidade em (m): "))
volume_retirado = float(input("Qual foi o volume retirado da piscina (L)? : "))

volume_m3 = calcular_volume_m3 (largura, comprimento, profundidade )
volume_litros = volume_m3 *1000

restante = volume_restante(volume_litros, volume_retirado)

print (f"volume total da piscina: {volume_litros:.0f} litros.")
print (f"volume retirado: {volume_retirado} litros.")
print (f"volume restante: {restante:.0f} litros.")
