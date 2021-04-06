código_peça_1 = input().split()
cp1 = int(código_peça_1[0])
np1 = int(código_peça_1[1])
vp1 = float(código_peça_1[2])
total1 = np1 * vp1

código_peça_2 = input().split()
cp2 = int(código_peça_2[0])
np2 = int(código_peça_2[1])
vp2 = float(código_peça_2[2])
total2 = np2 * vp2

soma_total = total1 + total2
print(f'VALOR A PAGAR: R$ {soma_total:.2f}')
