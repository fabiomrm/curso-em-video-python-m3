#Programa com função "fatorial()" que recebe dois parâmetros:
#1. Número a calcular
#2. show - valor lógico (opcional) se será mostrado na tela o processo de cálculo


def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print(f'=', end=' ')

        f *= c
    return f


print(fatorial(5, True))
