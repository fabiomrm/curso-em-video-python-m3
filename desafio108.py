#Formate os valores do 107 agora como moeda

from úteis.utilidadescev import moeda, dados

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {moeda.moeda(p)} em 10% temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo p em 20% temos {moeda.moeda(moeda.diminuir(p,20))}')