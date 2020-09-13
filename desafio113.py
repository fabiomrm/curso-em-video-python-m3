#Reescrever a função leiaInt() do desafio 104, incluindo a possibilidade da digitação de um número inválida
#Crie a função "leiafloat()" que faz o mesmo.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário decidiu não digitar valor. \033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR! Digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário decidiu não digitar valor. \033[m')
            return 0
        else:
            return n









#Programa principal

num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar os números {num1} e {num2} ')
