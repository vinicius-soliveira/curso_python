"""
Listas são estruturas similares a arrays, com a diferença
de serem dinâmicas, isto é, não possuem tamanho fixo.
As listas, não possuem tipo de dado fizo podem comportar
uma conjunto de qualquer tipo de dado.

As listas são representadas por colchetes: []

"""

#Exemplo lista com os 10 primeiros numeros primos:

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(primos)

#Exemplo lista com as letras de uma palavra:

soletrando = list('Vinicius')
print(soletrando)

# Verificando se um valor está contido em uma lista

if 6 in primos:
    print("6 é primo")
else:
    print("6 não é primo")
    
# Ordenando os termos de uma lista: método sort()

lista1 = [3, 1, 7, 99, 2, 4, 12, 5, 14, 0] 
print(lista1)
lista1.sort()
print(lista1)

# Adicionando um elemento a lista: método append()
lista2 = ['uva', 'maçã', 'pera', 'laranja']
print(lista2)
lista2.append('manga') # apenas um elemento por vez
print(lista2)
lista2.append(['banana', 'goiaba', 'caju']) # adiciona uma lista dentro de uma lista
print(lista2)

# Para adicionar os elementos de uma lista a outra lista: método extend()
lista3 = ['uva', 'maçã', 'pera', 'laranja']
print(lista3)
lista3.extend([1, 2, 3, 's']) 
print(lista3)
    