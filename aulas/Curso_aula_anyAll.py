'''
Any e All

any e all são funções integradas do Python.

A função any() retorna True se qualquer elemento do iterável
for verdadeiro. Se o iterável estiver vazio, retorna False.

A função all() retorna True se todos os elementos de um iterável
são verdadeiros ou ainda se o iterável está vazio.
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