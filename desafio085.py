#Programa que permite digitação de 07 valores numéricos e cadastre em uma única lista.
#Mostra separadamente os pares e os ímpares em ordem crescente
numeros = []
dados_par = []
dados_impar = []
c = 0
n = 0
while c < 7:
    valor = int(input(f'Digite o {c + 1}º número: '))
    if valor % 2 == 0:
        dados_par.append(valor)
    else:
        dados_impar.append(valor)
    c += 1
numeros.append(dados_par[:])
numeros.append(dados_impar[:])
print(f'Os números pares digitados, em ordem crescente, foram: {sorted(numeros[0])}')
print(f'Os números ímpares digitados, em ordem crescente, foram: {sorted(numeros[1])}')






