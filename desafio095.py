#desafio 93, mas pede dados de vários jogadores
jogador = {}
gols = []
gols_detalhe = []
lista = []
while True:
    c = 0
    soma_gols = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    while c < partidas:
        num_gols = int(input(f'Quantos gols na partida {c + 1}? '))
        soma_gols += num_gols
        gols.append(num_gols)
        c += 1
    jogador['gols'] = gols.copy()
    gols.clear()
    jogador['total'] = soma_gols
    lista.append(jogador.copy())
    pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
    print('-' * 30)
    if pergunta == 'N':
        break
print(lista)
print(f'{"cod":<7}{"nome":<7}{"gols":^5}{"total":>10}')
print('-' * 30)
for i, n in enumerate(lista):
    print(f'{i+1}      {lista[i]["nome"]:5}   {lista[i]["gols"]} {lista[i]["total"]:^5}')
print('-' * 30)
print(gols)
while True:
    pergunta2 = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if pergunta2 != 999:
        if (pergunta2 - 1) > i or (pergunta2 - 1) < 0:
            print('Jogador inválido')
        else:
            indice = pergunta2 - 1
            print(f'-- Detalhes do jogador: {lista[indice]["nome"]} ')
            for a in range(0, len(lista[indice]["gols"])):
                print(f'No jogo {a + 1} fez {lista[indice]["gols"][a]} gols')
    else:
        break
print('FIM DO PROGRAMA')




