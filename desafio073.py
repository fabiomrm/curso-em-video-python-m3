#Tupla preenchida com os 20 primeiros colocados na tabela do brasileirão. Mostre:
#1. Apenas os 05 primeiros colocados
#2. Os últimos 04 colocados
#3. Lista em ordem alfabética
#4. Em que posição está o time do Bragantino
top20 = ('Vasco', 'Internacional', 'Atlético Mg', 'Bahia', 'Santos', 'Atlético Pr', 'Grêmio'
         'Botafogo', 'Palmeiras', 'Bragantino', 'Corinthias', 'Atlético Go', 'São Paulo', 'Fluminense',
         'Fortaleza', 'Sport', 'Flamengo', 'Goiás', 'Ceará', 'Coritiba')
#1.
print(f'Os 05 primeiros colocados são: {top20[0:5]}')
#2.
print(f'Os 04 últimos colocados são: {top20[-4:]}')
#3.
print(f'Em ordem alfabética temos: {sorted(top20)}')
#4
time = str(input('Deseja saber a posição de qual time? ')).strip().title()
if time in top20:
    posicao = top20.index(time) + 1
    if posicao == 1:
        print(f'O {time} é o líder!')
    else:
        print(f'O time {time} está na {posicao}ª posição.')

else:
    print('Time não está disputando o campeonato.')