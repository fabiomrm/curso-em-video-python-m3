#Programa que lê 05 valores e cadastre-os em uma lista, já na posição crescente, sem usar sort().
#No final, mostra a lista ordenada.
num = []
maior = menor = posicao = 0
cont = 1
for valor in range(0, 5):
    valor = int(input('Digite um número: '))
    if cont == 1:
        num.append(valor)
        cont += 1
        print(f'O número {valor} foi o primeiro a ser inserido.')
    else:
        if valor > max(num):
            posicao = len(num)
            num.insert(posicao, valor)
            cont += 1
            print(f'O número {valor} foi adicionado ao final da lista')
        elif valor < min(num):
            posicao = 0
            num.insert(posicao, valor)
            cont += 1
            print(f'O número {valor} foi inserido no início da lista')
        elif min(num) < valor < max(num):
            for c in range(0, len(num)):
                c += 1
                if valor < num[c]:
                    break
            posicao = c
            num.insert(posicao, valor)
            print(f'O número {valor} foi inserido na posição {posicao}')
            cont += 1
            c = 0
print(f'A lista em ordem fica {num}')
