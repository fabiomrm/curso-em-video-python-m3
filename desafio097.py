#Programa que tenha uma função "escreva()" que recebe texto e mostra msg com tamanho adaptável.
def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


#Programa principal
escreva('Oi')
escreva('Fábio Marcone')
escreva('Curso em Vídeo Python')

