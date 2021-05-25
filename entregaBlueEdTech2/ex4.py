#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva
#  uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 
# 'data inválida' caso a data seja inválida.
meses = [['janeiro', 1], ['fevereiro', 2], ['março', 3], ['abril', 4], ['maio', 5],['junho', 6],
['julho', 7],['agosto', 8], ['setembro', 9],['outubro', 10],['novembro', 11],['dezembro', 12]]

dia = int(input('digite o dia (ex:01 a 31): ').strip())
mes = int(input('digite o mes (ex:01 a 12): ').strip())
ano = int(input('digite o ano (ex: 2021): ').strip())

if dia < 32 and dia > 0 and mes < 13 and mes > 0 and ano > 0 and ano < 10000:
    for m in meses:
        if mes == 1:
            if m[1] == 1:
                print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
            if mes == 2:
                if m[1] == 2 and dia < 30:
                    print(f'{dia} de {m[0]} de {ano}')
                elif mes == 2 and dia > 29:
                    print('Data inválida')
                    break
    for m in meses:
        if mes == 3:
            if m[1] == 3:
                 print(f'{dia} de {m[0]} de {ano}')           
    for m in meses:
        if mes == 4:
            if m[1] == 4:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 5:
            if m[1] == 5:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 6:
            if m[1] == 6:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 7:
            if m[1] == 7:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 8:
            if m[1] == 8:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 9:
            if m[1] == 9:
                 print(f'{dia} de {m[0]} de {ano}')            
    for m in meses:
        if mes == 10:
            if m[1] == 10:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 11:
            if m[1] == 11:
                 print(f'{dia} de {m[0]} de {ano}')
    for m in meses:
        if mes == 12:
            if m[1] == 12:
                 print(f'{dia} de {m[0]} de {ano}')
else:
    print('Data inválida!') 
