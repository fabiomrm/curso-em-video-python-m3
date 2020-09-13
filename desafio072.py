#Programa que tenha uma tupla preenchida por contagem por extenso de 0 até 20
#Lê o número digitado e mostra por extenso
numeros_ext = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'catorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente!', end=' ')
print(f'O número digitado foi {numeros_ext[num]}.')



