"""
List Comprehensions servem para gerar novas listas com dados processados a partir de outro iterável.
Basicamente list comprehensions é uma ferramenta bastante poderosa para realiazar processamento sobre 
listas,tuplas, strings, ranges, etc.
Sintaxe:

[dado for dado in iteravel]

Nested lists são listas de listas, similar a matrizes em outras linguagens de programação
Sintaxe: [[elementos primeira linha], [elementos segunda linha]], também podem ser gerados por
meio de list comprehension.

Dict Comprehension é uma estrutura análoga a list comprehension, só que aplicada a dicionários
Sintaxe: {chave: valor for valor in iteravel}


Set Comprehension  uma estrutura análoga a list comprehension, só que aplicada a conjuntos
Sintaxe: {valor for valor in iteravel}

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

# Outro exemplo utilizando list comprehension
print("\nOutro exemplo - utilizando list comprehension")

tupla = [(v1, v2) for v1 in numeros for v2 in amigos]
print(tupla)


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

# Criando nested list

print("\nExemplo - criando nested list")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

print("\nExemplo - criando nested list utilizando nested list")
matriz = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(matriz)

# Acessando nested list
print("\nExemplo - acessando nested list")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz)
print(matriz[0][2])
print(matriz[2][1])

# Iterando sobre nested lists
print("\nExemplo - iterando sobre nested list")
for lista in matriz:
    for i in lista:
        print(i)

print("\nExemplo - iterando sobre nested list utilizando list comprehension")

[[print(valor) for valor in lista] for lista in matriz]

################################ Dict Comprehension #############################

# Utilizando Dict Comprehension
print("\nExemplo - Utilizando Dict Comprehension\n")

dicionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()}
print(dicionario)
print(quadrado)

lista = [1,2,3,4,5]
quadrado = {valor: valor ** 2 for valor in lista}
print(lista)
print(quadrado)

# Utilizando Dict Comprehension condicionais
print("\nExemplo - Utilizando Dict Comprehension com condicionais\n")

numeros = [1,2,3,4,5]
res = {num: ('impar' if num % 2 else 'par') for num in numeros}
print(res)

################################ Set Comprehension #############################

# Utilizando Set Comprehension
print("\nExemplo - Utilizando Set Comprehension\n")
numeros = {num for num in range(1,10)}
print(numeros)

letras = {letra for letra in 'Vinicius Oliveira'}
print(letras)
