''''
Tuplas são estruturas similares a listas com a distinção de serem imutáveis,
isto é, os elementos não são editáveis, não podendo adicionar elementos, remover 
elementos, mudar o valor de um elemento e toda operação sobre uma tupla gera outra tupla.
Tuplas devem ser utilizadas sempre que não for preciso modificar os dados contidos na coleção
Tuplas são mais rápidas que listas.
Tuplas são representadas por parenteses, mas podem ser criadas sem os parenteses

'''

# Criando tuplas
print("\nExemplo - criando tuplas\n")
tupla1 = (1,2,3,4) 
print(tupla1, type(tupla1))
tupla2 = 2,3,5,7
print(tupla2, type(tupla2))
tupla_unitaria = 0, #Tuplas são definidas por virgulas e não parenteses
print(tupla_unitaria, type(tupla_unitaria))
tupla = tuple(range(6)) # Criando tupla a partir de um range
print(tupla, type(tupla))

# Desempacotamento de tuplas
print("\nExemplo - desempacotando tuplas\n")
stop = ('Ana', 'Acre', 'Abacaxi')
nome, lugar, fruta = stop 
print(stop, nome, lugar, fruta)
print("\nDesempacotando para variáveis e listas")
numeros = tuple(range(11))
primeiro, segundo, *resto = numeros
print(numeros, primeiro, segundo, resto)

# Se a tupla é numerica suporta operações matemáticas
print("\nExemplo - operações matemáticas tuplas\n")
tupla_num = 4,5,7,3,7,2,1
print(f'A soma dos elementos da tupla é {sum(tupla_num)}')
print(f'O maior valor da tupla é {max(tupla_num)}')
print(f'O menor valor da tupla é {min(tupla_num)}')

# Concatenação de tuplas
print("\nExemplo - concatenação de tuplas\n")
tupla3 = 7,8,6
tupla4 = 'oi', 'bom dia', 'boa noite'
tupla3 = tupla3 + tupla4
print(tupla3)

# Iterando sobre uma tupla
print("\nExemplo - iterações sobre tuplas\n")
impares = 1,3,5,7,9,11
print("Utilizando for")
for n in impares:
    print(n, end = ' ')
  
print("\n\nUtilizando while")   
dias_uteis = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')
i=0
while i < len(dias_uteis):
    print(dias_uteis[i], end=' ')
    i+=1
    
# Copiando uma tupla para outra
print("\n\nExemplo - copiando tuplas\n")
tupla5 = 1,2,3,4,5
print(tupla5)
nova = tupla5 # Não tem o problema de shallow copy
print("\nDeep Copy")
print(nova)
print(tupla5)

outra = 6,7,8,9
nova +=outra
print(nova)
print(tupla5)

