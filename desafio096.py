#Programa que tenha uma função chamada área()
#Recebe largura e comprimento e retorna área
def area(l, c):
    a = float(l * c)
    print(f'A área de um terreno {l:.2f}x{c:.2f} m é de {a:.2f} m²')


#Programa principal
print(f'CONTROLE DE TERRENOS')
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
