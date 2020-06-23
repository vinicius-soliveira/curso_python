'''
any() é uma função integrada que retorna True se qualquer elemento do iterável
for verdadeiro. Se o iterável estiver vazio, retorna False.

all() é uma função integrada que retorna True se todos os elementos de um iterável
são verdadeiros ou ainda se o iterável está vazio.

max() é uma função integrada que retorna o maior valor em um iterável ou o maior
de dois ou mais números.

min() é uma função integrada que retorna o menor valor em um iterável ou o maior
de dois ou mais números.

len() é uma função integrada que retorna o tamanho (número de itens)
de um iterável.

abs() é uma função integrada que retorna o valor absoluto de um número
inteiro ou real.

sum() é uma função integrada que retorna a soma dos valores de um iterável numérico
recebe um valor inicial.

round() é uma função integrada que retorna um número arredondado para n digitos de precisão,
por default retorna o inteiro mais próximo.

sorted() é uma função integrada com finalidade de ordenar qualquer iterável.
sorted retorna uma lista com os elementos do iterável ordenados
sorted não altera o iteravel original.

reversed é uma função integrada com finalidade de reverter a ordem de qualquer iterável.

zip() é uma função integrada que retorna um iterável gerado a partir da agregação de n
iteraveis dados como parametros de entrada. Retorna um iteravel formado por tuplas com
os k-esimos elementos de cada iteravel de entrada.

'''
############### Utilizando any ########################
print(" ")
print("Exemplo: utilizando any")
print(" ")
print(any([0,1,2,3,4,5]))
print(any([0, False, {}, [], ()]))
nomes = ['Vinicius', 'Vanessa', 'Walter', 'Vitor', 'Dilma', 'Zeca']
print(any(nome[0] == 'W' for nome in nomes))

############### Utilizando all ########################
print(" ")
print("Exemplo: utilizando all")
print(" ")
print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))
print(all(nome[0] == 'V' for nome in nomes))

############### Utilizando min ########################
print(" ")
print("Exemplo: utilizando min")
print(" ")
lista = [5,40,3,96,12]
print(min(lista))
dic = {'a':850, 'b':120, 'c':15}
print(min(dic))
print(min(dic.values()))
persona = ['Reddington', 'Keen', 'Rostova', 'Ressler', 'Cooper', 'Zuma']
print(min(persona))
print(min(persona, key=lambda nome: len(nome)))

############### Utilizando max ########################
print(" ")
print("Exemplo: utilizando max")
print(" ")
print(max(lista))
dic = {'a': 45, 'b':120, 'c':15}
print(max(dic))
print(max(dic.values()))
persona = ['Reddington', 'Keen', 'Rostova', 'Ressler', 'Cooper']
print(max(persona))
print(max(persona, key=lambda nome: len(nome)))

############### Utilizando len ########################
print(" ")
print("Exemplo: utilizando len")
print(" ")
print(len(lista))
print(len(persona))
print(len(persona[0]))
print('Vinicius'.__len__())

############### Utilizando abs ########################
print(" ")
print("Exemplo: utilizando abs")
print(" ")
print(abs(40))
print(abs(-40))
print(abs(-40.0))


############### Utilizando sum ########################
print(" ")
print("Exemplo: utilizando sum")
print(" ")
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5], 6))
print(sum([2.365, 4.586]))

############### Utilizando round ########################
print(" ")
print("Exemplo: utilizando round")
print(" ")
print(round(10.45))
print(round(10.54))
print(round(10.4899, 2))

########### Utilizando sorted ###########################
print(" ")
print("Exemplo: utilizando sorted")
print(" ")
numeros = (9, 1, 6, 3, 15, 0)
print(numeros)
print(sorted(numeros))

########### Ordenando em ordem decrescente
print(sorted(numeros, reverse = True))

########### Utilizando reversed ###########################
print(" ")
print("Exemplo: utilizando reversed")
print(" ")
print(list(reversed(numeros)))
print(tuple(reversed(numeros)))

########### Utilizando reversed em loops ###########################
print(" ")
print("Exemplo: utilizando reversed")
print(" ")

for i in reversed(range(10)):
    print(i)

########### Utilizando zip ###########################
print(" ")
print("Exemplo: utilizando zip")
print(" ")
lista1 = [2, 4, 5, 9,10]
lista2 = [3, 4, 6, 9, 13]
zip1 = zip(lista1, lista2)
print(list(zip1))

########### Um outro exemplo utilizando zip ###########################
print(" ")
print("Um outro exemplo utilizando zip")
print(" ")
lista = [2, 4, 5, 9, 10]
tupla = (3, 4, 6, 9, 25)
conjunto = {8, 6, 10, 1, 3} 
dicionario = {'a': 7, 'b': 6,'c': 14,'d': 2,'e': 3}
zip2 = zip(lista, tupla, conjunto, dicionario.values()) 
print(list(zip2))
########### Um outro exemplo utilizando zip_longest ###########################
print(" ")
print("Um outro exemplo utilizando zip")
print(" ")

from itertools import zip_longest

print("utilizando zip")
lista1 = [2, 4, 5]
lista2 = [3, 4, 6, 9, 13]
zip1 = zip(lista1, lista2)
print(list(zip1))
print("\nutilizando zip_longest")
lista1 = [2, 4, 5]
lista2 = [3, 4, 6, 9, 13]
zip2 = zip_longest(lista1, lista2, fillvalue='*')
print(list(zip2))