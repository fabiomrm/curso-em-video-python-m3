#Formate o desafio 108 modificando as funções criadas no 107,
#para que elas aceitem mais um parâmetro,
#informando se o valor vai ser formatado pela função moeda() do desafio 108

from úteis.utilidadescev import moeda, dados

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metadenovo(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobronovo(p,True)}')
print(f'Aumentando {moeda.moeda(p)} em 10% temos {moeda.aumentarnovo(p,10,True)}')
print(f'Diminuindo p em 20% temos {moeda.diminuirnovo(p,20,True)}')