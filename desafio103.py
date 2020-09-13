#Programa com a função "ficha(), com dois parâmetros: nome e qnt. gols
#Deve ser capaz de mostrar a ficha mesmo que algum dado não tenha sido informado


def ficha(a, b):
    if a == '':
        a = '<desconhecido>'
    if b == '':
        b = 0
    return f'O jogador {a} fez {b} gol(s) no campeonato.'


#Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: ' ))
print(ficha(nome, gols))
