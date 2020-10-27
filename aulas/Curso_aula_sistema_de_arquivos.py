'''
Python oferece um módulo chamado os que serve para fazer uso de manipulação 
de arquivos do sistema operacional.

O método getcwd() retorna o diretório em que o script está salvo.
O método chdir() é uma função utilizada para alterar o diretório.
O atributo name retorna o nome do sistema operacional (posix = linux ou macos)
ou nt = windows.
O método uname() retorna informações sobre o sistema operacional
O método path.join une um diretório absoluto a um relativo ou um arquivo. 
Pode ser utilizado para acessar um subdiretório ou arquivo.
O método listdir lista os arquivos e subdiretórios armazenados no diretório raiz
O método path.exists verifica a existencia de um arquivo ou diretório.
O método mknod() é utilizado para criar um arquivo
O método mkdir() é utilizado para criar um diretório
O método makedirs() é utilizado para criar um diretório dentro de outro
Na criação de arquivos e diretórios, caso já exista algum arquivo/diretório com o mesmo
nome, irá ocorrer um erro do tipo FileExistsError.
O método path.getsize() retorna o tamanho do arquivo em bytes
O método rename() é utilizado para renomear arquivos e diretórios vazios. 
O método remove() é utilizado para excluir um arquivo
O método rmdir() é utilizado para excluir um diretório vazio
O método removedirs() é utilizado para excluir um diretório com arquivos
Ao excluir um arquivo/diretório com python, a exclusão é permanente, e para mandar 
um arquivo/diretório é preciso utilizar o módulo send2trash
Para trabalhar com arquivos temporários é necessário utilizar o módulo tempfile
Para mover e copiar arquivos é necessário utilizar o módulo shutil
'''

import os
import sys
from send2trash import send2trash
from tempfile import TemporaryDirectory, TemporaryFile
from shutil import move, copy


# Obtendo o endereço do diretório atual
print("\nObtendo o endereço do diretório atual:", end = " ")
print(os.getcwd())

# Alterando o endereço do diretório atual
print("\nAlterando o endereço do diretório atual:", end = " " )
os.chdir('..')
print(os.getcwd())
teste = os.path.join(os.getcwd(), 'aulas')
os.chdir(teste)
print(os.getcwd())

# Identificando o sistema operacional
print("\nIdentificando o sistema operacional:", end = " ")
print(os.name)
print("Identificando o sistema operacional:", end = " ")
print(sys.platform)

# Obtendo informações sobre o sistema operacional
print("\nObtendo informações sobre o sistema operacional:", end = " ")
print(os.uname()) 

# Listando diretórios e arquivos
print("\nListando diretórios e arquivos:")
print(f'Este diretório possui {len(os.listdir())} arquivos')
print(os.listdir()) 

# Verificando a existência de um arquivo ou diretorio
print("\nVerificando a existência de um arquivo ou diretorio:")
print(os.path.exists('arquivo.txt'))
#print(os,path.exists('ponteiros.txt'))

# Criando diretórios e arquivos
print("\nCriando diretórios e arquivos:")
os.mkdir('Arquivo')
os.makedirs('Arquivos/Modelos')
os.mknod('arquivo2.txt')

# Renomeando arquivos e diretórios 
print("\nRenomeando diretórios e arquivos:")
os.rename('arquivo2.txt', 'teste.txt') 
os.rename('Arquivo', 'Views')  

# Removendo arquivos 
print("\nRemovendo arquivos:")
os.remove('teste.txt') 

# Removendo diretórios 
print("\nRemovendo diretórios:")
os.rmdir('Views') 

# Removendo árvore de diretórios 
print("\nRemovendo diretórios:")
os.removedirs('Arquivos/Modelos') 

# Removendo arquivos para a lixeira
print('\nRemovendo arquivos para lixeira')
os.mknod('arquivo2.txt')
send2trash('arquivo2.txt')

# Trabalhando com arquivos temporários
print('\nTrabalhando com arquivos temporários')

with TemporaryDirectory() as tmp:
    print(f'Diretório temporário criado em {tmp}')
    with  open(os.path.join(tmp, 'arquivo_temporario.txt'), 'a') as arquivo:
        arquivo.write("Olá, Mundo!!!")

with TemporaryFile() as tmpfile:
    tmpfile.write(b'Ola Mundo!!!\n')
    tmpfile.seek(0)
    print(tmpfile.read())

# Movendo e copiando arquivos
print('\nMovendo arquivos')
with  open('arquivo_teste.txt', 'a') as arquivo:
        arquivo.write("Olá, Mundo!!!")
with  open('arquivo_teste2.txt', 'a') as arquivo:
        arquivo.write("Olá, Mundo!!!")
try:
    os.mkdir('Nova Pasta')
except FileExistsError:
    print('A pasta já foi criada')

move('arquivo_teste.txt', 'Nova Pasta/arquivo_teste.txt')
copy('arquivo_teste2.txt', 'Nova Pasta/arquivo_teste2.txt')