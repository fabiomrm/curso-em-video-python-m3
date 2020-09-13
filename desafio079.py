#Programa que pede valores e adiciona apenas os que não forem repetidos. Mostra em ordem crescente
num = []
while True:
    novo_num = int(input('Digite um valor: '))
    if novo_num not in num:
        num.append(novo_num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já foi inserido na lista!')
    pergunta = str(input('Deseja continuar[S/N]: ')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if pergunta == 'N':
        break

print(sorted(num)) #Quando forem itens iteráveis, deve-se usar sorted(list) e não list.sort()

