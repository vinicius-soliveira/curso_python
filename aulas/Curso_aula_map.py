'''
Map 

map é uma função integrada do Python que é utilizada para fazer
mapeamento de valores para uma função.
map é uma função que recebe dois parametros: o primeiro a função,
e o segundo o iteravel.

A função map retorna um iterável formado pelo valor da função
aplicada a cada valor do itéravel que gerou o objeto Map.

'''

############### Utilizando map ########################
print(" ")
print("Exemplo: utilizando map")
print(" ")
import math
def area(r):
    """ Calcula a área de um circulo com raio r """
    return math.pi * (r**2)

raios = [2, 3.5, 6, 1, 10.5]
areas = map(area, raios)
print(list(areas)) 

################# Map com lambda ######################
print(" ")
print("Exemplo: Map com lambda")
print(" ")
print(list(map(lambda r: math.pi * (r ** 2), raios)))

################# Mais um exemplo de maps ######################
print(" ")
print("Mais um exemplo com map")
print(" ")
cidades = [('João Pessoa', 28), ('São Paulo', 12), ('Rio de Janeiro', 30), ('Fortaleza', 35)]
print(cidades)
print(" ")
degC_to_degF =  lambda dado: (dado[0], 1.8*dado[1]+32)
print(list(map(degC_to_degF, cidades)))
print(" ")