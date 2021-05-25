#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

resp = list()
respostas = 0
resp.append(input('Telefonou para a vítima?(S/N) ').upper().strip())
resp.append(input('Esteve no local do crime?(S/N) ').upper().strip())
resp.append(input('Mora perto da vítima?(S/N) ').upper().strip())
resp.append(input('Devia para a vítima(S/N) ').upper().strip())
resp.append(input('Já trabalhou com a vítima?(S/N) ').upper().strip())
for r in resp:
        if r == 'S':
                respostas += 1
if respostas == 2:
        print('O interrogado(a) é: Suspeito(a)')
elif respostas == 3 or respostas == 4:
        print('O interrogado(a) é: Cúmplice')
elif respostas == 5:
        print('O interrogado(a) é: Assassino')
else:
        print('O interrogado(a) é: Inocente')
