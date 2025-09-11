valor_emprestimo = float(input('Digite o valor desejado para o emprestimo: R$'))
num_parcelas = int (input('Digite a quantidade de parcelas desejadas (6 a 36):'))
renda_mensal = float (input ('digite sua renda mensal: R$'))


valor_parcelas = valor_emprestimo / num_parcelas
renda_permitida = renda_mensal * 0.3

if valor_emprestimo < 1000 or valor_emprestimo > 50000:
    resultado = 'Emprestimo não aprovado: valor fora dos limites permitidos.'

elif num_parcelas < 6 or num_parcelas > 36: 
    resultado = 'Emprestimo não aprovado: quantidade de parcelas invalida'

elif valor_parcelas > renda_permitida:
    resultado = f'emprestimo não aprovado: valor das parcelas excede 30% da renda mensal'
else:
    resultado = f'emprestimo aprovado. valor das parcelas: R$ {valor_parcelas:.2f}'
print('\nResultado:')
print(resultado)
