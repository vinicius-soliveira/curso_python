'''
Funções são pequenas partes de um programa que realizam uma determinada tarefa neste programa.
Funções podem ou não receber entrada de dados e retornar um saída de dados.
Funções são bastante utilizadas quando um programa faz muitas ações repetidas ou similares.

Para definir uma função em Python:

def nome_funcao(parametros_de_entrada):
    corpo_da_função

def é uma palavra reservada do Python que indica a definição de uma função
O nome da função é sempre com letras minusculas e se for composto deve ser separado por underline (snake case)
Os parametros de entrada são opcionais e caso tenha mais de um, devem ser separados por virgula

Uma ferramenta interessante em Python são as Docstrings que servem pra documentar as funções.
A documentação é feita através de comentários entre """ """. E a documentação pode ser acessada
por meio de __doc__

Os parâmetros com valores default são postos sempre após os parametros
de valor definido pelo usuário. Isto permite que a função seja flexivel
e evita erros com parametros incorretos.
Os parâmetros com valores default pode ser de qualquer tipo de dado,
inclusive listas, tuplas, dicionários e funções 

O *args é um parâmetro de função em Python que coloca os valores extras informados como entrada
em uma tupla. O args é chamado da seguinte forma: *nome_do_parametro, mas por conveção
é utilizado *args.

O **kwargs é um parâmetro de função em Python que exige parâmetros nomeados e que coloca os valores
extras informados como entrada em um dicionário. O kwargs é chamado da seguinte forma:
**nome_do_parametro, mas por conveção é utilizado **kwargs.

Nas funções, os parâmetros tem ordem de inserção:
Parametros obrigatórios -> *args -> Parametros padrões -> **kwargs

'''
# Definindo funções
def hello_world(): # Função sem entrada e sem retorno
    print("\nHello World\n") #A função criada utiliza uma função built-in Python
  
def hello_world(): # Função sem entrada e com retorno
    return '\nHello World'

def lista(): #Uma função pode retornar diversos valores
    return 1, '2', (3,4,5), [6,7,8,9]
   
from random import random   
def cara_ou_coroa(): #Uma função pode ter mais de um return
    """Função que gera pseudoaleatoriamente um resultado de arremesso de cara ou coroa"""
    if random() <0.5:
        return 'cara'
    return 'coroa'

def par_impar(numero): # Função com entrada e retorno
    return 'ímpar' if numero%2 else 'par'

def soma(a,b): # Função com vários dados de entrada
    return a+b

def nome_completo (nome, sobrenome): # Função com argumentos nomeados
    return f'O nome completo é {nome} {sobrenome}'

def potencia(base, expoente=1): #Função com parametro padrão
    return base ** expoente

def soma(a=0,b=0): # Função com vários dados de entrada
    return a+b

def subtracao(a=0,b=0): # Função com vários dados de entrada
    return a-b


def operacao(num1, num2, fun=soma): # Função com uma função como parâmetro padrão
    return fun(num1, num2)
 
def func(*args):
    print(args)
    
def multiplica(*args):
    if args:
        produto = 1
        for i in args:
            produto *=i
        else: return produto
    else: return 0       
     
def signos(**kwargs):
    print(kwargs)
    
def cadastro(nome, idade, *args, solteiro = True, **kwargs):
    print(f'\nParametros obrigatórios: {nome} tem {idade} anos')
    print(f'\n*args: {args}')
    if solteiro:
        print('\nParametro default: Solteiro')
    else:
        print('\nParametro default: Casado')
    print(f'\n**kwargs: {kwargs}')

def desempacota_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"
   
#Executando funções
print("\nExecutando função sem entrada e sem retorno")
hello_world()
ola = hello_world #variavel recebendo a função
ola()

print("\nExecutando função sem entrada e com retorno")
ola = hello_world()+'!' #variavel recebendo o valor de retorno da função
print(hello_world())
print(ola)

print("\nFunção retornando diferente tipos de dados")
print(lista())

print("\nFunção para verificar se um número é par ou ímpar")
print(f' 1 é {par_impar(1)}')
print(f' 4 é {par_impar(4)}')
print(f' 128 é {par_impar(128)}')

print('\nExemplo - argumentos nomeados')
print(nome_completo(sobrenome='Oliveira', nome = 'Vinicius')) # Função com argumentos nomeados

print('\nExemplo - parametro padrão')
# Exemplo com 1 parametro padrão
print("\nExemplo de uma função com um parametro padrão")
print(potencia(4,5))
print(potencia(7)) #utiliza o parametro padrão

# Exemplo com mais de 1 parametro padrão
print("\nExemplo de uma função com um parametro padrão")
print(soma(3,8))
print(soma(9))
print(soma(*[1,8]))#lista desempacotada como parametro
print(soma())

# Exemplo de uma função como parametro padrão
print("\nExemplo de uma função como parametro padrão")
print(operacao(5,6))
print(operacao(10,6, subtracao))

# Exemplo - Docstring
print(f'\n{cara_ou_coroa.__doc__}\n')

# Exemplo - *args
print("\nExemplo -*args")
func()
func(1)
func(2,3,4)
func(5,6,7,8,9)

print("\nExemplo - desempacotamento *args")
numeros = [7,1,6,9,4,5]

print(multiplica())
print(multiplica(2,3))
print(multiplica(4,5,6))
print(multiplica(*numeros))

# Exemplo - **kwargs
print("\nExemplo -**kwargs")

signos(vinicius='gemeos', luana = 'sagitário', joão = 'áries', lara = 'touro')

print('\nExemplo - oredem dos parâmetros \n')
cadastro('Vinicius', 26)
cadastro('Vinicius', 26, 1.71, 'Estudante', 'Gosta de animais')
cadastro('Vinicius', 26, 1.71,  'Gosta de animais', solteiro =False,python = 'sim')

# Exemplo -  desempacotamento **kwargs
print("\nExemplo - desempacotamento **kwargs")

nomes = {'nome': 'Vinicius', 'sobrenome': 'Oliveira'}
print(desempacota_nomes(**nomes))
