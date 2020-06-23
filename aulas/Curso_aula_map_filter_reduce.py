'''
Map 

map é uma função integrada do Python que é utilizada para fazer
mapeamento de valores para uma função.
map é uma função que recebe dois parametros: o primeiro a função,
e o segundo o iteravel.

A função map retorna um iterável formado pelo valor da função
aplicada a cada valor do itéravel que gerou o objeto Map.

Filter é uma função integrada do Python e é utilizada para filtrar
dados de uma determinada coleção.

Reduce não é uma função integrada do Python3, apeans no Python2.
Entretanto é possivel utilizar esta função importando o módulo
functools.

Reduce é utilizada para retornar um valor sobre um iterável a
partir de uma função.

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

############### Utilizando filter ########################
print(" ")
print("Exemplo: utilizando filter")
print(" ")

valores = 1,2,3,4,5,6,7,8
media = sum(valores)/len(valores)
print(media)
acima_da_media =filter(lambda x: x > media, valores)
print(list(acima_da_media))

############ Exemplo: remoção de dados faltantes ##########
print(" ")
print("Exemplo: remoção de dados faltantes")
print(" ")
estados = ['', 'Acre', '', 'Ceará', 'Goiás', '','', 'Pará']
print(estados)
estado = filter(None, estados)
print(list(estado))

############ Exemplo mais complexo ########################
print(" ")
print("Exemplo mais complexo")
print(" ")

inscritos = [
    {'nome': 'Adam', 'idade': 25, 'cidade': 'São Paulo'},
    {'nome': 'Laura', 'idade': 17, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Carlos', 'idade': 32, 'cidade': 'Vitória'},
    {'nome': 'João', 'idade': 14, 'cidade': 'Recife'},
    {'nome': 'Rebeca', 'idade': 16, 'cidade': 'Curitiba'},
    {'nome': 'Tiago', 'idade': 21, 'cidade': 'Fortaleza'},
]
print(inscritos)
# Só aceita os maiores de idade
selecionados =  filter(lambda dados: dados['idade'] >= 18, inscritos)
print(list(selecionados))

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

