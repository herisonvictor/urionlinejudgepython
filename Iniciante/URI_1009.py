nome = str(input())
s_fixo = float(input())
vendas = float(input())
comissão = vendas * 0.15
montante_total = comissão + s_fixo
print(f'TOTAL = R$ {montante_total:.2f}')
