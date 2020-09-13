#Programa que lê NOME, IDADE e SEXO de várias pessoas
#Cada pessoa é um dicionário e todos os dicionários em uma lista. Mostra:
#1. Quantas pessoas foram cadastradas
#2. Média de idade do grupo
#3. Lista com todas as mulheres
#4. Lista com pessoas com idade acima da média
dicionario = {}
cadastro = []
lista_mulheres = []
while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while dicionario['sexo'] not in 'MF':
        dicionario['sexo'] = str(input('Sexo [M/F]: '))
    dicionario['idade'] = int(input('Idade: '))
    cadastro.append(dicionario.copy())
    if dicionario['sexo'] == 'F':
        lista_mulheres.append(dicionario['nome'])
    pergunta = str(input('Quer continuar [S/N]? ')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N]? ')).strip().upper()
    if pergunta == 'N':
        break
print(cadastro)

#1.
print(f'- O grupo possui {len(cadastro)} pessoas.')
#2.
s_idade = 0
for c in range(0, len(cadastro)):
    s_idade += cadastro[c]['idade']
media = s_idade/len(cadastro)
print(f'- A média de idades é: {media:.1f} anos.')
#3.
print('- As mulheres cadastradas foram:', end=' ')
for i, m in enumerate(lista_mulheres):
    print(m.upper(), end=' ')
print()
#4.
print('- As pessoas com a média de idade acima da média são: ')
for i in range(0, len(cadastro)):
    if cadastro[i]['idade'] > media:
            print(f'nome = {cadastro[i]["nome"]}; sexo = {cadastro[i]["sexo"]}; '
                  f'idade = {cadastro[i]["idade"]}')
    i+=1


