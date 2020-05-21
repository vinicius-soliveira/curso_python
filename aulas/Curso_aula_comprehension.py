"""
List Comprehensions servem para gerar novas listas com dados processados a partir de outro iterável.
Basicamente list comprehensions é uma ferramenta bastante poderosa para realiazar processamento sobre 
listas,tuplas, strings, ranges, etc.

Sintaxe:

[dado for dado in iteravel]

Nested lists são listas de listas, similar a matrizes em outras linguagens de programação

"""

################################ List Comprehension ##########################

# Utilizando list comprehension
print("\nExemplo - utilizando list comprehension")

numeros = [1,2,3,4,5]
res = [numero*10 for numero in numeros]
print(numeros) 
print(res)

# List comprehension vs loops
print("\nExemplo - método análogo utilizando loops")

numeros = [1,2,3,4,5]
res = []
for numero in numeros:
    res.append(numero*10)

print(numeros) 
print(res)

# Outro exemplo utilizando list comprehension
print("\nOutro exemplo - utilizando list comprehension")

amigos = 'vinicius', 'brendon', 'tiago', 'junior'
res = [amigo.capitalize() for amigo in amigos]
print(res)

# Exemplo - utilizando condicionais em list comprehensions
print("\nExemplo - utilizando condicionais em list comprehensions")

import math

def primo(num):
    divisores=0
    for i in range(2,math.ceil(math.sqrt(10))+1):
        if num == 2: break
        if num % i==0:
            divisores+=1
            break
    if not divisores and num !=1:
        return True
    else:
        False
    
numeros = range(1,100,1)
primos = [numero for numero in numeros if primo(numero)]
print(primos)

################################## Nested List ##################################

