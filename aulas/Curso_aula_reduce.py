'''
Reduce

Reduce não é uma função integrada do Python3, apeans no Python2.
Entretanto é possivel utilizar esta função importando o módulo
functools.

Reduce é utilizada para retornar um valor sobre um iterável a
partir de uma função.
 
'''
############### Utilizando reduce ########################
print(" ")
print("Exemplo: utilizando reduce")
print(" ")

from functools import reduce

dados = [2,3,5,7,11,13,17,23,29] 
multi = lambda x,y: x*y 
produto = reduce(multi, dados)
print(produto)  

############### Uma solução alternativa ########################
print(" ")
print("Uma solução alternativa")
print(" ")

produto = 1
for n in dados:
    produto*=n
print(produto)