#Desafio 86, ao final mostrando:
#1. Soma dos valores pares
#2. Soma dos valores da coluna 3
#3. Maior valor da linha 2
matriz = []
temp = []
coluna3 = []
linha2 = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        temp.append(int(input(f'Digite um valor para {[linha, coluna]}: ')))
        if coluna == 2:
            coluna3.append(temp[:])
        if linha == 1:
            linha2.append(temp[:])
        matriz.append(temp[:])
        temp.clear()
print(f'MATRIZ: \n{matriz[0]} {matriz[1]} {matriz[2]}\n'
      f'{matriz[3]} {matriz[4]} {matriz[5]}\n'
      f'{matriz[6]} {matriz[7]} {matriz[8]} ')
#1. Soma dos pares
s_pares = 0
for c in range(0, 9):
    if matriz[c][0] % 2 == 0:
        s_pares += matriz[c][0]
print(f'A soma dos valores pares é: {s_pares}')
#2. Soma coluna 3
soma = 0
for s in range(0, 3):
    soma += coluna3[s][0]
print(f'A soma dos valores da coluna 3 é: {soma}')
#3. Maior valor linha 2
for a in range(0, 3):
    if a == 0:
        maior = linha2[a][0]
    else:
        if linha2[a][0] > maior:
            maior = linha2[a][0]
print(f'O maior valor na linha 2 é: {maior}')


