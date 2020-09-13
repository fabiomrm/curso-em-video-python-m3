#Programa com função "maior()" que recebe vários parâmetros
#Analisa qual o maior valor

def maior(* num):
    print('Analisando os valores passados...')
    for i, n in enumerate(num):
        print(n, end=' ')
    if num == 0:
        print(f'Não foi informado nenhum número.')
    print(f'Foram informados {len(num)} números.')
    print(f'O maior valor informado foi {max(num)}.')
    print('-=' * 15)


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(1, 7, 92)
maior(4, 7, 0)
maior(1, 2)
maior()
