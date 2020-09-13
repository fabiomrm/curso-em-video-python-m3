#Programa com função "notas()" e vai retornar um dicionário com as informações:
#1. Quantidade de notas
#2. Maior nota
#3. Menor nota
#4. Média turma
#5. Situação (OPCIONAL)



def notas(*n, sit=False):
    """
    -> Analisa notas de alunos
    :param n: uma ou mais notas de alunos
    :param sit: valor opcional, indica se o aluno foi aprovado, reprovado ou recuperação
    :return: dicionário com informações diversas
    """
    import math
    dict = {}
    soma = 0
    c = 0
    while c < len(n):
        soma += n[c]
        c += 1
    dict['total'] = len(n)
    dict['maior'] = max(n)
    dict['menor'] = min(n)
    dict['média'] = soma / len(n)
    if sit == True:
        if dict['média'] >= 7:
            dict['situação'] = 'APROVADO'
        elif dict['média'] < 4:
            dict['situação'] = 'REPROVADO'
        else:
            dict['situação'] = 'RECUPERAÇÃO'
    return dict


#Programa principal
resp = notas(3.5, 10, 6.5, sit=True)
print(resp)
