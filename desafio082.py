#Programa que lê números, e depois mostra três listas:
#números digitados, números pares e números ímpares
numeros = []
numeros_pares = []
numeros_impares = []

while True:
    numeros.append(int(input('Digite um número: ')))
    pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if pergunta == 'N':
        break
print(f'A lista é formada pelos seguintes números: {numeros}')

for c, valor in enumerate(numeros):
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)
print(f'A lista de números pares contidos na lista é: {numeros_pares}')
print(f'A lista de números ímpares contidos na lista é: {numeros_impares}')