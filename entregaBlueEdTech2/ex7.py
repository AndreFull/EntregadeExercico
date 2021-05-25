#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores 
# pares e ímpares em ordem crescente.

listanum = []
par = []
impar = []
for c in range(0,7):
    num = (int(input('Digite um valor: ')))
    listanum.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 != 0:
        impar.append(num)
        listanum.sort()
print(f'Os valores pares são: {par}')
print(f'Os valores impares são: {impar}')
print(f'A lista em ordem crescente é: {listanum}')
