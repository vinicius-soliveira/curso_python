'''
Python possui funções built-in para leitura e escrita em arquivos de texto.

A função open() abre/cria um arquivo de texto (cria um objeto arquivo de texto), para isto é passado como
parametro, o caminho do arquivo. Por padrão o arquivo é aberto em
modo de leitura, podemos passar parametros para configurar como queirar:

r -> Abre para leitura
w -> Abre para escrita, e adiciona o texto no inicio do arquivo
x -> Abre para escrita somente se o arquivo não existir, caso exista gera FileExistsError
a -> Abre para escrita, e adiciona o texto sempre ao final do arquivo

A função read() retorna uma string com todo o conteudo de um arquivo de texto

A função readline() retorna uma string com o conteudo de uma determinada linha do texto.

A função seek() é utilizada para movimentar o cursor pelo arquivo, recebe como parametro o
n-ésimo caractere.

o bloco with é utilizado para criar um ambiente para se trabalhar com texto
Utilizar o bloco with é uma boa prática de programação em python

StringIO é utilizado para criar arquivos em memória. Não é uma função built-in do Python
sendo necessário importar o modulo io

'''

#Criando e escrevendo em um arquivo de texto
print('\nCriando e escrevendo em um arquivo de texto:')
arquivo = open('arquivo.txt', 'w+')
arquivo.write("Estou aprendendo a manipular arquivos em Python!!!\n")
arquivo.write("Que bacana!\nLogo mais serei expert em Python.\n")
arquivo.write("E poderei desenvolver softwares bastante interesssantes.")

# Abrindo e lendo o conteúdo de um arquivo
print('\nLendo todo conteudo de um arquivo de texto:\n')
arquivo.seek(0)
print(arquivo.read())

# Movimentando o cursor pelo arquivo
print('\nMovimentando o cursor pelo arquivo')
print('Retornando o início do texto e imprimindo a primeira linha:\n')   
arquivo.seek(0)
print(arquivo.readline()) # imprime a primeira linha de texto
print('Movimentando o cursor para a terceira linha e imprimindo o texto')
arquivo.seek(62)
print(arquivo.read())

# Descobrindo o numero de linhas de um texto
print('\nDescobrindo o numero de linhas de um texto\n')
arquivo.seek(0)    
linhas = arquivo.readlines()
print(f'O texto possui {len(linhas)} linhas de texto')

arquivo.close()

# Trabalhando com with 
print('\nUtilizando bloco with para manipular arquivos\n')
with open("arquivo.txt") as arquivo:
    print(arquivo.read())


########### Utilizando StringIO #################
from io import StringIO as strio

mensagem = '\nEsta mensagem é secreta. Não leia!'
arq = strio(mensagem)
print(arq.read())