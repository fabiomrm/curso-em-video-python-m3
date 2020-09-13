#Programa que lê quatro valores no teclado e guarde-os numa tupla. Mostra:
#1. Quantas vezes aparece 9
#2. Posição do primeiro 3
#3. Quais números são pares
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
#1.
procura9 = 9 in tupla
if procura9 == True:
    print(f' O número 9 aparece {tupla.count(9)} vezes')
else:
    print(f'O número 9 não foi digitado.')
#2.
procura3 = 3 in tupla
if procura3 == True:
    print(f'O primeiro 3 aparece na posição {tupla.index(3)}')
else:
    print(f'O número 3 não foi digitado em nenhuma posição')
#3.
c = 0
print('Os valores pares digitados são:', end=' ')
while c < len(tupla):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
        c += 1
    else:
        c += 1









