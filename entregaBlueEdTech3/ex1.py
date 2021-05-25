#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o 
   # resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
soma = num1 + num2
mult = num1 * num2
div = num1 // num2
print(f'A soma dos dois valores é:{soma}')
print(f'A multiplicação entre os valores é: {mult}')
print(f'A divisão inteira deles é: {div}')
if num1 > num2:
    print(f'O maior dos dois números é:{num1}')
else:
    print(f'O maior dos dois números é:{num2}')
if soma % 2 == 0:
    print('O resultado da soma dos números é um número par')
else:
    print('O resultado da soma dos números é um número impar')
if div == 0:
    print('O resultado é ZERO')
elif mult > 40:
    print(f'A multiplicação dos dois números dividido pelo resultado da sua divisão inteira é {mult / div}')
else:
    print('A multiplicação foi menor que 40')