#Programa que gerencia o aproveitamento de um jogador de futebol:
#Lê o nome do jogador, quantas partidas jogou, gols/partida.
#Guarda tudo em um dicionário, inclusive a quantidade de gols no campeonato
jogador = {}
gols = []
soma_gols = 0
c = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
while c < partidas:
    num_gols = int(input(f'Quantos gols na partida {c + 1}? '))
    soma_gols += num_gols
    gols.append(num_gols)
    c += 1
jogador['gols'] = gols.copy()
jogador['total'] = soma_gols
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
print('Nelas, seu saldo foi: ')

for i, g in enumerate(gols):
    print(f' => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {soma_gols} gols.')


