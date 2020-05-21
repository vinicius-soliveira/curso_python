"""
Módulos Collections é um módulo de coleções do Python que oferece
alternativas as coleções built-in do Python(listas, tuplas, diconários e conjuntos)

Collections: High-performance Container Datatypes

Counter: recebe um iterável  como parametro e gera um objeto similar a
um dicionário, contendo como chave, um elemento do iterável passado como 
parâmetro, e como valor a quantidade de ocorrencias desse elemento.

Default Dict: retorna um objeto dicionário, ao gerar um dicionário uilizando, tem como um dos parametros um valor
default, podendo utilizar um lamba para isso. Este valor será utilizado sempre que
não houver um valor definido. Caso uma chave inexistente tente ser acessada, esta
chave será criada e o valor default será atribuido a ela.

Ordered Dict - retorna um objeto dicionário com ordem de inserção garantida.
Todos os métodos para dicionários funcionam para Default Dict e Ordered Dict

Named Tuple - retorna uma tupla diferenciada com um nome para a tupla e seus parametros
Todos os métodos para tuplas funcionam para Named Tuple

Deque  - é uma lista de alta performance

"""
# Utilizando colletions

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque
lista = [1,2,2,3,3,3,4,4,4,4,5,7,11,13]

################################# Counter ################################
print("\nExemplo - Counter")
cont = Counter(lista)
print(cont,type(cont))

print("\nExemplo - Counter: texto")

texto = '''
Vento solar e estrelas do mar
A terra azul da cor do seu vestido
Vento solar e estrelas do mar
Você ainda quer morar comigo

Sol, girassol, verde, vento solar
Você ainda quer morar comigo
Vento solar e estrelas do mar
Um girassol da cor de seu cabelo

'''
palavras = texto.split()
cont2 = Counter(palavras)
print(cont2,type(cont2))

################################# Default Dict ###########################
print("\nExemplo - Default Dict")
dicionario = defaultdict(lambda:0)
dicionario['nome'] = 'Vinicius'
print(dicionario,type(dicionario))

################################# Ordered Dict ###########################
print("\nExemplo - Ordered Dict")
ord_dic = OrderedDict({'a':1, 'b':2, 'c':3})
print(ord_dic,type(ord_dic))

for chave,valor in ord_dic.items():
    print(f'chave={chave}:valor={valor}')

print("\nExemplo - Diferença entre Dict e Ordered Dict")

print('\nDict')
dic1 = {1:2,3:4}
dic2 = {3:4, 1:2}
print(f'{dic1} é igual a {dic2}:{dic1==dic2}')

print('\nOrdered Dict')
ordic1 = OrderedDict({1:2,3:4})
ordic2 = OrderedDict({3:4, 1:2})
print(f'{ordic1} é igual a {ordic2}:{ordic1==ordic2}')

################################# Named Tuple ###########################
print("\nExemplo - Named Tuple")
# Formas de declarar uma namedtuple
pessoa = namedtuple('pessoa', 'nome idade profissao')
pessoa = namedtuple('pessoa', 'nome, idade, profissao')
pessoa = namedtuple('pessoa', ['nome', 'idade', 'profissao'])

print("\nCriando um objeto namedtuple")
vini = pessoa(nome='Vinicius', idade = 26, profissao = 'Estudante')
print(vini, type(vini))

################################# Deque ###########################
print("\nExemplo - Deque")
# criando um deque
deq =  deque('vinicius')
print(deq,type(deq))