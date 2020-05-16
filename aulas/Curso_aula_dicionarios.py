"""
Dicionários são coleções do tipo chave/valor em que estas estão explicitas.

Dicionários são representados por chaves: {} e chave e valor são separados por :
    {chave: valor}
    Chave e valor podem ser de qualquer tipo de dado, e um dicionário pode ser
    formado por dados de diferentes tipos.
    Cada chave é única(não permite repetições) e  está vinculada a apenas um valor
"""

# Criando um dicionário
times = {'crf': 'Flamengo', 'sccp':'Corinthians', 'fcb': 'Barcelona'}
print(times, type(times))

times = dict(crf = 'Flamengo', sccp = 'Cortinthians', fcb = 'Barcelona')
print(times, type(times))

# Dicionários podem ser formados por diferentes tipos de dados
dic = {42:'int', 13.8:'float', (1,2):'tupla', 'oi':'str'}
print(dic,type(dic))

# Acessando os elementos de um dicionário
print(times['crf']) #acesso via chave 
print(times.get('fcb')) # acessando via método get (mais recomendado)
print(times.get('spfc')) # retorna None quando a chave não é contida no dicionário

# Adicionar elementos ao um dicionário
lucro_mensal = {'jan': 1200, 'fev': 1500, 'mar': 800}
print(lucro_mensal,type(lucro_mensal))
lucro_mensal['abr'] = 300
print(lucro_mensal,type(lucro_mensal))
lucro_mensal.update({'mai':200})
print(lucro_mensal,type(lucro_mensal))

# Atualizar dados de um um dicionário
lucro_mensal['abr']=250
print(lucro_mensal,type(lucro_mensal))
lucro_mensal.update({'mai':120})
print(lucro_mensal,type(lucro_mensal))

# Remover dados de um dicionário

lucro_mensal.pop('mai') # Remove o valor vinculado a chave do dicionário e o retorna
print(lucro_mensal,type(lucro_mensal))
del lucro_mensal['abr']
print(lucro_mensal,type(lucro_mensal))


