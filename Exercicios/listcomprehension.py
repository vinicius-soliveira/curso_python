string = '01234567890123456789012345678901234567890123456789'

lista = [string[0:10] for i in range(6)]
retorno = '.'.join(lista)
print(lista)
print(retorno)