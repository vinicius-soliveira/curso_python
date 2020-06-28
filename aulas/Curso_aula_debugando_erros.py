'''
---------------------------------------------------------------------------
Os erros mais comuns em Python:

SintaxError: Ocorre quando o Python encontra um erro de sintaxe,
isto é, o Python não reconhece o comando. 

NameError: Ocorre quando uma váriavel ou função foi utlizada sem
previamente ser definida. 

TypeError: Ocorre quando uma função/operação é aplicada a um tipo
errado.

IndexError: Ocorre quando tentamos acessar um elemento em uma lista
ou outro tipo de dado indexado utilizando um indice inválido.

ValueError: Ocorre quando uma função built-in recebe um argumento com
tipo correto mas valor inapropriado.

KeyError: Ocorre quando tentamos acessar um dicionário com uma chave 
que não existe.

AttributeError: Ocorre quando uma váriavel não tem um atributo/método.

IndentationError: Ocorre quando não é respeitada a indentação do Python.
------------------------------------------------------------------------------

Levantar os próprios erros:

raise é uma palavra reservada do Python que tem como utilidade a criação
de exceções e mensagens de erro. O raise assim como o return finaliza a 
função.
------------------------------------------------------------------------------

Tratando erros:

Para tratar os erros que podem ocorrer no código em Python é utilizado o 
bloco try/except. Com isto previne que o programa pare de funcionar e o 
usuário receba mensagens de erro.

Uma principal fonte de erros em um software é a entrada de dados, desta
forma toda entrada deve ser tratada.

Em um bloco try/except pode ser adicionado um comando else que é apenas 
executado caso não ocorra uma exceção.

O comando finally é sempre executado. independente se houve exceção ou não,
geralmente é utilizado para fechar ou desalocar recursos.
--------------------------------------------------------------------------------- 

Python Debugger



'''
################## Utilizando raise #######################
print(" ")
print("Exemplo: utilizando raise")
print(" ")
def colore(texto, cor):
    cores = 'amarelo','azul', 'branco', 'verde', 'vermelho'
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if not cor in cores:
        raise ValueError(f'A cor precisa ser {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')
    
colore('Vinicius','azul')

################# Utilizando try/except - forma genérica #######################
print(" ")
print("Exemplo: utilizando try/except - forma genérica")
print(" ")
try:
    teste()
except:
    print('Deu algum problema')    
    
try:
    sorted(5,8,6)
except:
    print('Deu algum problema')  
    
################# Utilizando try/except - forma especifica #######################
print(" ")
print("Exemplo: utilizando try/except - forma especifica")
print(" ")
try:
    sum(5, 'a')
except TypeError:
    print('Deu algum problema')    
 
import math
    
try:
    divide(12, 4)
except NameError:
    print('Deu algum problema')  
    
try:
    x = -10
    print(f'A raiz quadrada de {x} é {math.sqrt(x)}')
except ValueError as err:
    print(f'A aplicação gerou o seguinte erro: {err}') 

######### Utilizando try/except - tratando vários erros ########
print(" ")
print("Exemplo: utilizando try/except - tratando vários erros")
print(" ") 

try:
    len(8)
    teste()
except NameError as erro_1:
    print(f'A aplicação gerou o seguinte erro: {erro_1}')
except TypeError as erro_2:
    print(f'A aplicação gerou o seguinte erro: {erro_2}')  
    
############ Mais um exemplo utilizando try/except #############
print(" ")
print("Mais um exemplo utilizando try/except")
print(" ") 

def pega_valor(dicionário, chave):
    try:
        return dicionário[chave]
    except KeyError as erro_3:
        return  print(f'A aplicação gerou o seguinte erro: {erro_3}')  
    except TypeError as erro_4:
        return  print(f'A aplicação gerou o seguinte erro: {erro_4}')  
    except Exception as erro_5:
        return print(f'Ocorreu um erro inesperado')
            
dic = {'nome': 'Vinícius', 'idade': 27}

print(pega_valor(dic,'nome'))
print(pega_valor(dic,'lugar'))

############ Tratando dados de entrada #########################
print(" ")
print("Tratando dados de entrada")
print(" ")

try:
    num = int(input('Informe um número: '))
except:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')   
      
############ Tratando entrada de dados de função #########################
print(" ")
print("Tratando entrada de dados de função")
print(" ")

def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'Ocorreu um problema: {erro}'

num1 = input('Informe um número: ')
num2 = input('Informe um número: ')

print(dividir(num1, num2))

