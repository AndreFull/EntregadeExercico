# 05 - Refatore o exercício 2, para que uma função receba uma frase, faça todo o tratamento necessário 
# e retornar o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas
# da frase original.

frase  =  str(input( 'Digite uma frase:' )).lower()
a  =  0
e  =  0
i  =  0
o  =  0
u  =  0
for b in frase :
    if b   == 'a' :
        a  +=  1
    if  b  ==  'e' :
        e  +=  1
    if  b  == 'i' :
        i  +=  1
    if  b  == 'o' :
        b  +=  1
    if  b  == 'u' :
        u  +=  1             
volret  = ( a + e + i + o + u )        
print( f'A quantidade de letras A digitadas e que foram retiradas é: { a } ' )
print( f'A quantidade de letras E digitadas e que foram retiradas é: { e } ' )
print( f'A quantidade de letras I digitadas e que foram retiradas é: { i } ' )
print( f'A quantidade de letras O digitadas e que foram retiradas é: { o } ' )
print( f'A quantidade de letras U digitadas e que foram retiradas é: { u } ' )
print( '- ='  *  20 )
for  b in "aeiou" :
    frase  =  frase.replace( b , "" )
print( f'A frase sem vogais fica: { frase } ' )
print( '- ='  *  20 )
print( f'A quantidade total de vogais retiradas é: { volret } ' )