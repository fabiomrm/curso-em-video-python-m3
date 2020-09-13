#Programa que lê nome e duas notas de vários alunos
#Boletim contendo média de cada usuário e que permite ver a nota de cada um isoladamente
nome = []
nota = []
media = []
cadastro = []
alunos = []
while True:
    cadastro.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    media = (nota[0] + nota[1])/2
    cadastro.append(nota[:])
    cadastro.append(media)
    alunos.append(cadastro[:])
    nome.clear()
    nota.clear()
    cadastro.clear()
    pergunta = str(input('Deseja continuar[S/N]? ')).strip().upper()
    if pergunta in 'N':
        break
print(alunos)
print(len(alunos))
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for c, p in enumerate(alunos):
    print(f'{c + 1:<4}{p[0]:<10}{p[2]:>8.1f}')
print('-' * 30)

while True:
    pergunta2 = int(input('Deseja ver as nota de qual aluno? (999 interrompe) '))
    if pergunta2 > len(alunos):
        print(f'Digite um número de aluno válido.')
    elif pergunta2 == 999:
        print('FINALIZANDO...')
        break
    else:
        print(f'As notas de {alunos[pergunta2 - 1][0]} foram {alunos[pergunta2 -1][1]}')
print('FIM')






