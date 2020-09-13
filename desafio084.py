#Programa que lê nome e peso de várias pessoas. Mostra:
#1. Quantas pessoas foram cadastradas
#2. Lista das pessoas mais pesadas
#3. Lista das pessoas mais leves
pessoas = []
cont_pessoas = 0
dados = []
p_pesados = []
p_leves = []
pergunta = ''
while True:
        dados.append(str(input('Digite nome: ')))
        dados.append(int(input('Digite peso: ')))
        pessoas.append(dados[:])
        cont_pessoas += 1
        pergunta = str(input('Deseja adicionar mais alguém?[S/N] ')).upper().strip()
        for c in range(0, len(pessoas)):
                if c == 0:
                        maior_peso = pessoas[c][1]
                        menor_peso = pessoas[c][1]
                        dados.clear()
                if pessoas[c][1] > maior_peso:
                        maior_peso = pessoas[c][1]
                if pessoas[c][1] < menor_peso:
                        menor_peso = pessoas[c][1]
                c += 1
        dados.clear()
        while pergunta not in 'SN':
                pergunta = str(input('Deseja adicionar mais alguém?[S/N] ')).upper().strip()
        if pergunta == 'N':
                break
print(f'Foram cadastradas {cont_pessoas} pessoas!')
print(pessoas)

dados2 = []
p_pesados = []
p_leves = []
for p in range(0, len(pessoas)):
        if maior_peso == pessoas[p][1]:
                dados2.append(pessoas[p][0])
                p_pesados.append(dados2[:])
                dados2.clear()
        if menor_peso == pessoas[p][1]:
                dados2.append(pessoas[p][0])
                p_leves.append(dados2[:])
                dados2.clear()
        p += 1
print(f'Com {maior_peso} kgs, os cadastrados com maior peso foram: {p_pesados} ')
print(f'Com {menor_peso} kgs, os cadastrados com menor peso foram: {p_leves} ')








    
