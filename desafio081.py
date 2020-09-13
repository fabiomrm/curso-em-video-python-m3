#Programa que lê números e coloca em uma lista. Mostra
#1. Quantos números foram digitados
#2. Lista em ordem decrescente
#3. Se o valor 5 está ou não na lista
numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    cont += 1
    pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if pergunta == 'N':
        break
#1.
print(f'Foram digitados {cont} números')
#2.
print(f'A lista em ordem decrescente: {sorted(numeros, reverse=True)}')
#3.
check5 = 5 in numeros
if check5 == True:
    print(f'O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')





