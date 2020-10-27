'''
Em Python, módulos são bibliotecas que possuem um conjunto de funções.
Módulos são úteis na reutilização de código.

Módulo random possui varias funções para geração de numeros pseudo-aleatórios
ou funções que sorteiam um elemento de um iteravel.

Algumas funções são random, randint, uniform, choice, shuffle

A função random gera um número aleatório entre 0 e 1.
A função randint gera um numero inteiro aleatório dentro de um dado intervalo
A função uniform gera um numero aleatório dentro de um dado intervalo
A função choice retorna um valor entre um iteravel
A função shuffle embaralha valores de um iteravel ordenavel.
'''

from random import random, randint, uniform, shuffle, choice

# Utilizando a função random
print("\nUtilizando a função random para gerar numeros aleatórios:")

for i in range(10):
    print(random(), end = ', ')

# Utilizando a função randint
print("\n\nUtilizando a função randint para gerar um jogo da mega sena:")

for i in range(6):
    print(randint(1,61), end = ', ')

# Utilizando a função uniform
print("\n\nUtilizando a função uniform para gerar numeros aleatórios:")


for i in range(10):
    print(uniform(2,8), end = ', ')

# Utilizando a função choice
print("\n\nUtilizando a função choice:")

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# Utilizando a função shuffle
print("\n\nUtilizando a função shuffle:")

cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(cartas)

shuffle(cartas)
print(cartas)
