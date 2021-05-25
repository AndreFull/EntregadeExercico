#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para 
# iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, 
# após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o 
# computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual 
# número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido 
# pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram 
# necessários para vencer.
from random import randint
senha = '180281'
verif_senha = input('Digite a senha correta: ').strip()
while verif_senha != senha:
    print('Senha incorreta, tente novamente!')
    verif_senha = input('Digite a senha para começar: ')
    if verif_senha == senha:
        print()
        
print('-=' * 20)      
print('Seja bem vindo!')
print('Você está no jogo da adivinhação!')
print('Tente adivinhar um numero entre 1 e 10')
print('Boa sorte!')
print('-=' * 20)
numero = str(randint(1,10))
c = 0
tentativa = 0
print(numero)
while numero != tentativa:
    c += 1 
    tentativa = str(input('Digite o numero correto: ')).strip()
    while tentativa < numero and tentativa != '10':
        print('Pensei em um número maior')
        tentativa = str(input('Digite o numero correto: ')).strip()
        c += 1
    while tentativa > numero or tentativa == '10':
        print('Tente um número menor')
        tentativa = str(input('Digite o numero correto: ')).strip()
        c += 1
print('* * ' * 12)
print('PARABÉNS!! Você acertou!')
print(f'Você acertou na {c} tentativa.')    
