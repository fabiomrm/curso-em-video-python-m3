#Programa que lê nome e média de 01 aluno
#Guarda a situação do aluno (sem perguntar)
#Se média >=7: Aprovado, se média <7: reprovado. No final mostra conteúdo da estrutura na tela
aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

