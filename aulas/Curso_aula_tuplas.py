''''
Tuplas são estruturas similares a listas com a distinção de serem imutáveis,
isto é, os elementos não são editáveis, não podendo adicionar elementos, remover 
elementos, mudar o valor de um elemento e toda operação sobre uma tupla gera outra tupla.
Tuplas devem ser utilizadas sempre que não for preciso modificar os dados contidos na coleção
Tuplas são mais rápidas que listas.
Tuplas são representadas por parenteses, mas podem ser criadas sem os parenteses

'''

# Criando tuplas
tupla1 = (1,2,3,4) 
print(tupla1, type(tupla1))
tupla2 = 2,3,5,7
print(tupla2, type(tupla2))
tupla_unitaria = 0, #Tuplas são definidas por virgulas e não parenteses
print(tupla_unitaria, type(tupla_unitaria))
tupla = tuple(range(6)) # Criando tupla a partir de um range
print(tupla, type(tupla))

# Desempacotamento de tuplas
stop = ('Ana', 'Acre', 'Abacaxi')
nome, lugar, fruta = stop 
print(stop)
print(nome, lugar, fruta)
numeros = tuple(range(11))
primeiro, segundo, *resto = numeros
print(numeros, primeiro, segundo, resto)

# Se a tupla é numerica suporta operações matemáticas
tupla_num = 4,5,7,3,7,2,1
print(sum(tupla_num))

# Concatenação de tuplas
tupla3 = 7,8,6
tupla4 = 'oi', 'bom dia', 'boa noite'
tupla3 = tupla3 + tupla4
print(tupla3)

# Iterando sobre uma tupla

impares = 1,3,5,7,9,11
for n in impares:
    print(n)
    
dias_uteis = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')
i=0
while i < len(dias_uteis):
    print(dias_uteis[i])
    i+=1
    
# Copiando uma tupla para outra
tupla5 = 1,2,3,4,5
print(tupla5)
nova = tupla5 # Não tem o problema de shallow copy

print(nova)
print(tupla5)

outra = 6,7,8,9
nova +=outra
print(nova)
print(tupla5)
