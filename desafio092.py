#Programa que lê: NOME, ANO DE NASCIMENTO (cadastra com idade) e CARTEIRA DE TRABALHO
#Se a CTPS for diferente de 0, o dicionário também receberá ANO DE CONTRATAÇÃO e SALÁRIO
#Calcule com quantos anos a pessoa irá se aposentar (depois de 35 anos de colaboração)
import datetime
hoje = datetime.datetime.today().year
dicionario = {}
while True:
    dicionario['nome'] = str(input('Nome: '))
    ano_nasc = int(input('Ano de nascimento: '))
    dicionario['idade'] = int(hoje - ano_nasc)
    dicionario['ctps'] = int(input('Número da CTPS [digite 0 caso não possua]: '))
    if dicionario['ctps'] == 0:
        break
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: R$ '))
    dicionario['aposentadoria'] = int(hoje - dicionario['contratação'] + 35)
    break
print(dicionario)
for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')

