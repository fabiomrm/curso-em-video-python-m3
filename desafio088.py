#Programa que ajuda um jogador da MEGA-SENA a criar palpites.
#Pergunta quantos jogos serão gerados e sorteia 6 números entre 1 e 60
#cadastra tudo em uma lista composta.

from random import sample
import time
jogo = []
temp = []
pergunta = int(input('Quantos jogos deseja cadastrar? '))
while len(jogo) < pergunta:
    jogo.append(sample(range(60), 6))
print(f'MEGA SENA')
time.sleep(1)
print(f'Computando jogos...')
time.sleep(1)
for n, a in enumerate(jogo):
    print(f'Jogo{n + 1}: {sorted(jogo[n])} ')
    time.sleep(1)
print('BOA SORTE!')



