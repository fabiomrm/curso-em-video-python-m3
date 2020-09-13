#Programa com função "voto()"
#Recebe o ano de nascimento, retornando se a pessoa tem voto NEGADO, OPCIONAL (>= 65) ou OBRIGATÓRIO



def voto(ano):
    from datetime import datetime
    print(f'-' * 30)
    hoje = datetime.today().year
    idade = hoje - ano
    if idade < 16:
        return f'Com idade {idade} anos: VOTO NEGADO'
    elif idade > 65 or 16 <= idade < 18:
        return f'Com idade {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com idade {idade} anos: VOTO OBRIGATÓRIO'



#Código principal
nasc = int(input('Digita ano de nascimento: '))
print(voto(nasc))




