"""
Utilizamos loops para iterar sobre sequencias ou
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
for letra in nome:
    print(letra.upper(), end = ' ')
 
print(' ')

#Exemplo 2
for num in lista:
    print(pow(num,2), end = ' ')
   
print(' ')   
 
#Exemplo 3 - no range o ultimo valor não é incluído   
for x in numeros:
    print(x, end = ' ')
    
print(' ') 

#Exemplo 4 - gera uma tupla com indice e valor do iteravel

for i in enumerate(nome[0:8]):
    print(i,end = ' ')  
    
