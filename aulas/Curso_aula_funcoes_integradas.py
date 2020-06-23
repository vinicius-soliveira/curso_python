'''

any e all são funções integradas do Python.

A função any() retorna True se qualquer elemento do iterável
for verdadeiro. Se o iterável estiver vazio, retorna False.

A função all() retorna True se todos os elementos de um iterável
são verdadeiros ou ainda se o iterável está vazio.

sorted é uma função integrada com finalidade de ordenar qualquer 
iterável em Python.
sorted retorna uma lista com os elementos do iterável ordenados
sorted não altera o iteravel original

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

########### Utilizando o Sorted ###########################
print(" ")
print("Exemplo: utilizando generator expressions")
print(" ")
numeros = (9,1,6,3)
print(numeros)
print(sorted(numeros))

########### Ordenando em ordem decrescente
print(sorted(numeros, reverse = True))
