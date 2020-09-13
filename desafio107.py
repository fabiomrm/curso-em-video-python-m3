#Programa que usa as funções de moeda.py

from úteis.utilidadescev import moeda, dados

p = float(input('Digite o preço: R$ '))
print(f'A metade de p é {moeda.metade(p)}')
print(f'O dobro de p é {moeda.dobro(p)}')
print(f'Aumentando p em 10% temos {moeda.aumentar(p,10)}')
print(f'Diminuindo p em 20% temos {moeda.diminuir(p,20)}')