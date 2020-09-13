#Programa que lê 5 valores e guarda numa lista
#Mostre o maior e o menor valor da lista, bem como suas posições.
num = []

for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print(f'A lista é composta pelos valores {num}')
print('\n')
maior = max(num)
menor = min(num)
print(f'O maior valor digitado foi {maior}, nas posições:', end=' ')
for c, valor in enumerate(num):
    if valor == maior:
        print(c, end='... ')
print('\n')
print(f'O menor valor digitado foi {menor}, nas posições:', end=' ')
for c, valor in enumerate(num):
    if valor == menor:
        print(c, end='... ')







