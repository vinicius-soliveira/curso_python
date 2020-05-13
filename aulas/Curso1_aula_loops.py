"""
Loops for são utilizados para iterar sobre sequencias ou
valores iteraveis, como:
strings
listas
ranges
enumerate

"""
nome = 'Vinicius Oliveira'
lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
numeros = range(1,10)

#Exemplo 1
print("Exemplo for em string")
for letra in nome:
    print(letra.upper(), end = ' ')
 
print(' ')

#Exemplo 2
print("Exemplo for em lista")
for num in lista:
    print(pow(num,2), end = ' ')
   
print(' ')   
 
#Exemplo 3 - no range o ultimo valor não é incluído
print("Exemplo for em range")   
for x in numeros:
    print(x, end = ' ')
    
print(' ') 

#Exemplo 4 - gera uma tupla com indice e valor do iteravel
print("Exemplo for em enumerate")
for i in enumerate(nome[0:8]):
    print(i,end = ' ')  
print(" ")    
"""
ranges são geradores de sequencia numerica de maneira
especificada (ordenada). Por padrão a sequencia é
iniciada em zero, o passo é sempre um inteiro, 
e o valor de parada não é incluso. Pode ser em ordem
crescente ou decrescente

A sintaxe do range pode ser:
range(valor_de_parada)
    nesse caso inicia em zero e vai com passo 1 até o
    valor de parada -1
    
range(valor_inicial,valor_de_parada) 
    nesse caso inicia no valor de início e vai com
    passo 1 até o valor de parada -1
    
range(valor_inicial,valor_de_parada, passo)
    nesse caso inicia no valor de início e vai com
    passo especificado até o valor de parada -1 

"""

"""
Loops while são utilizados para iterar sobre sequencias
    while expressão booleana:
            execução do loop

"""
#Exemplo 5
print("Exemplo while")
numero = 0

while numero < 10:
    print(numero, end = ' ')
    numero +=1
 
print(" ") 
 
"""
O comando break é utilizado para sair de um loop
de maneira "forçada".

O comando continue é utilizado com um desvio da
execução loop, não executando os comandos abaixo
e reinicia um novo ciclo. 

O comando pass é uma operação nula que pode ser utilizada
para reservar espaço para um futuro código
 
O comando else em loops é utilizado ao final do loop
seja por esgotamento de iteravel em um loop for ou por
uma condição falsa em loop while
 
"""
#Exemplo 6 - comando break
print("Exemplo break") 
for i in range(1,10):
    if i == 7:
         break # termina o loop aqui
    else:
         print(i, end = ' ')         
print("Saiu do loop")

#Exemplo 7 - comando continue
print("Exemplo continue") 

for i in range(1,10):
    if i == 7:
         continue # desvia loop aqui, retornando ao inicio
    print(i, end = ' ')
print(" ")
         
#Exemplo 8 - comando pass
print("Exemplo pass") 
for i in range(1,7):
    if i == 3:
        pass # reserva este ponto do loop
        print("Reservado", end =' ') 
    print(i, end = ' ')     
print(" ")        

#Exemplo 9 - comando else em loops
print("Exemplo else em loops") 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, '=', x, '*', int(n/x))
            break
    else:
        print(n, 'é um numero primo')