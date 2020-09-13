#Mini-sistema que utiliza o Interactive Help
#Usuário digita o comando e o manual vai aparecer
#Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

def pyhelp():
    from time import sleep
    while True:
        a = 'SISTEMA DE AJUDA PYHELP'
        print('\033[7;32m~\033[m' * len(a))
        print(f'\033[7;32mSISTEMA DE AJUDA PYHELP\033[m')
        print('\033[7;32m~\033[m' * len(a))
        msg = str(input('Função ou Biblioteca > ')).strip().lower()
        if msg == 'fim':
            print('ENCERRANDO PROGRAMA')
            break
        sleep(2)
        b = f'Acesso ao manual do comando {msg}'
        print(f'\033[7;35m~\033[m' * len(b))
        print(f'\033[7;36m{b}\033[m')
        print(f'\033[7;35m~\033[m' * len(b))
        sleep(2)
        help(msg)





pyhelp()


