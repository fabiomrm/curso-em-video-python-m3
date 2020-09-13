#Programa que cria uma matriz 3x3 e a preenche com valores lidos pelo teclado
matriz = []
temp = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        temp.append(int(input(f'Digite um valor para {[linha, coluna]}: ')))
        matriz.append(temp[:])
        temp.clear()
print(f'MATRIZ: \n{matriz[0]} {matriz[1]} {matriz[2]}\n'
      f'{matriz[3]} {matriz[4]} {matriz[5]}\n'
      f'{matriz[6]} {matriz[7]} {matriz[8]} ')
