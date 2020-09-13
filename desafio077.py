#Programa que diz quais vogais existem em cada palavra da tupla (sem acentos)
palavras = ('aprender', 'curso', 'grátis', 'python', 'linguagem', 'praticar', 'futuro', 'trabalhar',
            'mercado', 'programador', 'programar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra.upper(), end=' ')




