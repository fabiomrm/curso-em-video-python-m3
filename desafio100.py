#Programa com uma lista chamada números e duas funções:
#sorteio() e somapar()
#sorteio() vai sortear 5 números e colocá-los na lista
#somapar() vai mostrar a soma dos pares sorteados
from random import sample
numeros = sample(range(10), 5)

def sorteio():
    print('Sorteando os 05 valores da lista:', end=' ')
    for i, v in enumerate(numeros):
        print(f'{v}', end=' ')
    print()


def somapar():
    s_par = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            s_par += v
    print(f'Somando os valores pares de {numeros}, temos {s_par}')


#Programa principal
sorteio()
somapar()

