#Programa que gera 05 números aleatórios de 0 a 10 e coloca numa tupla
#mostra a listagem dos números e o maior valor da tupla
import random
maior = 0
menor = 0
num = 0
sorteio = random.sample(range(10), 5)
print('Os números sorteados foram:', end= ' ')
for num in sorteio:
    print(num, end=' ')
maior = max(sorteio)
menor = min(sorteio)
print(f'\nO maior valor é {maior} e o menor é {menor}')



