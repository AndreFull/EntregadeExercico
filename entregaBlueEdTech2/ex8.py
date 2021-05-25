#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
#  em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o
#  ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa
#  vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import date
pessoa = dict()
idade = 0
anoNasc = 0
dataAtual = date.today().year
pessoa['nome'] = str(input('Digite o nome: ')).title()
anoNasc = int(input('Digite o ano de nascimento(ex:2021): '))    
pessoa['anoNasc'] = anoNasc
idade = dataAtual - anoNasc    
pessoa['idade'] = idade
pessoa['ctps'] = int(input('Digite o número da CTPS: '))
if pessoa['ctps'] != 0:
    anoCont = int(input('Digite o ano de contratação(ex:2021): '))
    pessoa['salario'] = float(input('Digite o salário: '))
    pessoa['anoApos'] = anoCont - anoNasc + 35
print(f'O trabalhador {pessoa["nome"]}, que hoje tem {pessoa["idade"]} anos irá se aposentar com {pessoa["anoApos"]} anos')
