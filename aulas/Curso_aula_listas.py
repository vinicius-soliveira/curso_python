"""
Listas são estruturas similares a arrays, com a diferença de serem dinâmicas, isto é, não possuem tamanho fixo.
As listas, não possuem tipo de dado fizo podem comportar uma conjunto de qualquer tipo de dado.

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

# Acessando os elementos da string
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
print(lista[2]) #imprime a letra C 
    
# Ordenando os termos de uma lista: método sort()
lista1 = [3, 1, 7, 99, 2, 4, 12, 5, 14, 0] 
print(lista1)
lista1.sort()
print(lista1)

# Adicionando um elemento ao final da lista: método append()
lista2 = ['uva', 'maçã', 'pera', 'laranja']
print(lista2)
lista2.append('manga') # apenas um elemento por vez
print(lista2)
lista2.append(['banana', 'goiaba', 'caju']) # adiciona uma lista dentro de uma lista
print(lista2)

# Para adicionar o elementos de uma lista ao final de outra lista: método extend()
lista3 = ['uva', 'maçã', 'pera', 'laranja']
print(lista3)
lista3.extend([1, 2, 3, 's']) #tipo de dado dinâmico
print(lista3)
lista3 = lista3 + [10, 11, 12, 13] # uma maneira equivalente
print(lista3)
    
# Para adicionar um elemento na lista informando a posição método insert()
lista4 = [2, 4, 8, 32, 64, 128]
print(lista4)
lista4.insert(0, 1)
print(lista4)
lista4.insert(4, 16)
print(lista4)

# Para inverter uma lista
lista6 =[1,3,5,7,9,11,13,15,17,19]
print(lista6)
lista6.reverse()
print(lista6)
print(lista6[::-1]) # uma maneira alternativa

# Para copiar uma lista
lista7 = lista6.copy() # Deep Copy, as modificações nas listas são independentes
print(lista7)
lista7 = lista6 # Shallow Copy, a modificação em uma das listas reflete na outra
print(lista7)

# Para contar o numero de elementos de uma lista metodo len()
print(f"O tamanho da lista é {len(lista7)}")

#Para remover um elemento de uma lista
lista8 = list(range(4,60,4))
print(lista8)
lista8.pop() # remove o ultimo elemento da lista, _.pop() retorna o elemento removido
print(lista8) 
lista8.pop(6) # remove o elemento da posição 6 na lista, _.pop() retorna o elemento removido
print(lista8)
del(lista8[4]) ## remove o elemento da posição 4 na lista
print(lista8)
lista8.clear() # remove todos os elementos da lista
print(lista8)

#Convertendo string em lista, método split() 
frase = "A Terra azul da cor do seu vestido"
print(frase)
frase = frase.split() # por padrão o separador é o espaço, mas pode ser adotado outro
print(frase)

# Convertendo uma lista em string, método join
frase = " ".join(frase) # Transforma  a lista em string colocando espaço entre o
print(frase)

# Encontrar o indice de um determinado elemento na lista
lista9 = [0, 1,2,5,8,6,7,0,2,6,9,10,14,0]
print(lista9.index(6)) # retorna o indice da primeira ocorrencia do valor
print(lista9.index(2, 3)) # inicia a busca a partir do indice 3
print(lista9.index(0, 3, 9)) #faz a busca no intervalo entre 3 e 9 na lista

# Desempacotamento de lista

lista10 = [1,5,9]
num1,num2,num3 = lista10

print(lista10)
print(num1)
print(num2)
print(num3)

# Encontrando os valores de máximo e mínimo de uma lista
lista11 = [4, 8, 2, 19, 5, 0]
print(f'O valor máximo da lista é {max(lista11)}')
print(f'O valor máximo da lista é {min(lista11)}')