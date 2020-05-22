'''
Expressões lambdas são funções sem nome(anônimas)

Toda expressão lambda é iniciada pela palavra reservada lamba


'''

#Criando e utilizando lambdas
print("\nCriando e utilizando lambdas")
quadrado = lambda i: i ** 2 # maneira não interessante de uso de lambdas
print(quadrado(8))

print("\nCriando e utilizando lambdas")
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('vinicius', 'oliveira      '))

#Criando lambdas com vários parametros de entrada
print("\nExemplo - lambda com nenhuma entrada de dados")
saudacao = lambda:'Como vai você?'
print(saudacao())

print("\nExemplo - lambda com duas entradas de dados")
pitagoras = lambda x,y: (x ** 2  + y ** 2)** 0.5
print(pitagoras(4,3))

#Outro exemplo de lambdas
print("\nUtilizando lambdas da forma ideal\n")
autores = ['Aldous Huxley', 'Isaac Asimov', 'Fiodor Dostoievski', 'Machado de Assis', 'George Orwell']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

#Uso de lambda para funções matemáticas

def funcao_quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

fun = funcao_quadratica(1,4, -5)
print(fun(4))
print(fun(3))
print(fun(2))