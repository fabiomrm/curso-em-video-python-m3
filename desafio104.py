#Programa com a função "leiaint()"
#Funciona similar ao input(), mas faz validação para apenas valor númerico

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERROR! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor



#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')