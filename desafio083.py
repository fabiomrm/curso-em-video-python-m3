#Programa onde o usuário digita uma expressão usando parênteses
#analisa se a expressão está com os parênteses abertos e fechados na ordem correta
t = input(str('Digite uma expressão: '))
if '(' or ')' in t == True:
    p_aberto = t.count('(')
    print(p_aberto)
    p_fechado = t.count(')')
    print(p_fechado)

if p_aberto != p_fechado:
    print('Expressão inválida!')
else:
    print('Expressão válida')









