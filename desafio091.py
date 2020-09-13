#Programa em que 04 jogadores joguem um dado e tenham resultados aleatórios
#Guarda resultados em um dicionário, coloca o dicionário em ordem
from random import randint
from time import sleep
from operator import itemgetter #para ordenar dicionários
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('-' * 10)
print('RANKING DOS JOGADORES')
ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos')
    sleep(1)











