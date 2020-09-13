#Programa com função "contador()", que recebe 03 parâmetros: início, fim e passo
#Tem que fazer 03 contagens:
#1. De 01 até 10, de 1 em 1
#2. De 10 até 0, de 2 em 2
#3. Contagem personalizada
from time import sleep
def contador(i, f, p):
    print('-=' * 15)
    if p > 0:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        if i < f:
            c = i
            while c <= f:
                print(c, end=' ')
                sleep(1)
                c += p
        print()
        if i > f:
            c = i
            while c >= f:
                print(c, end=' ')
                sleep(1)
                c -= p
        print()
        print('-=' * 15)
    elif p < 0:
        print(f'Contagem de {i} até {f} de {-p} em {-p}')
        if i > f:
            c = i
            while c >= f:
                print(c, end=' ')
                sleep(1)
                c -= p
            print()
            print('-=' * 15)
    elif p == 0:
        p = 1
        print(f'Contagem de {i} até {f} de {p} em {p}')
        if i < f:
            c = i
            while c <= f:
                print(c, end=' ')
                sleep(1)
                c += p
        print()
        if i > f:
            c = i
            while c >= f:
                print(c, end=' ')
                sleep(1)
                c -= p
        print()
        print('-=' * 15)


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Valor inicial: '))
f = int(input('Valor final: '))
p = int(input('Passo: '))
contador(i, f, p)


