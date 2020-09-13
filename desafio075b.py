num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),int(input('Digite um valor: ')))

print(f'Você digitou os valores {num}')

print(f'O número 9 apareceu {num.count(9)}')

if 3 in num:
    print(f'O número 3 apareceu pela primeira vez na {num.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os números pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
