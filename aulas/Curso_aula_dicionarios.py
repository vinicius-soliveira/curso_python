"""
Dicionários são coleções do tipo chave/valor em que estas estão explicitas.
Dicionários são representados por chaves: {} e chave e valor são separados por :
    {chave: valor}
    Chave e valor podem ser de qualquer tipo de dado, e um dicionário pode ser
    formado por dados de diferentes tipos.
    Cada chave é única(não permite repetições) e está vinculada a apenas um valor
"""

# Criando um dicionário
print("\nExemplo - criando dicionários \n")
times = {'crf': 'Flamengo', 'sccp':'Corinthians', 'fcb': 'Barcelona'}
print(times, type(times))

times = dict(crf = 'Flamengo', sccp = 'Cortinthians', fcb = 'Barcelona')
print(times, type(times))

cadastro = {}.fromkeys(['nome', 'email',  'idade'], 'desconhecido')
print(cadastro, type(cadastro))

# Dicionários podem ser formados por diferentes tipos de dados
print("\nExemplo - dicionários com diferentes tipos de dados \n")
dic = {42:'int', 13.8:'float', (1,2):'tupla', 'oi':'str'}
print(dic,type(dic))

# Acessando os elementos de um dicionário

print("\nExemplo - acessando dicionários \n")

print(f"Acesso via chave: {times['crf']}") #acesso via chave 
print(f"Acesso via get(): {times.get('fcb')}") # acessando via método get (mais recomendado)
print(times.get('spfc')) # retorna None quando a chave não é contida no dicionário

# Adicionar elementos ao um dicionário

print("\nExemplo - adicionando elementos a um dicionário\n")
lucro_mensal = {'jan': 1200, 'fev': 1500, 'mar': 800}
print(lucro_mensal,type(lucro_mensal))
lucro_mensal['abr'] = 300
print(lucro_mensal,type(lucro_mensal))
lucro_mensal.update({'mai':200})
print(lucro_mensal,type(lucro_mensal))

# Atualizar dados de um um dicionário
print("\nExemplo - atualizando elementos de um dicionário\n")
lucro_mensal['abr']=250
print(lucro_mensal,type(lucro_mensal))
lucro_mensal.update({'mai':120})
print(lucro_mensal,type(lucro_mensal))

# Remover dados de um dicionário
print("\nExemplo - removendo elementos a um dicionário\n")
lucro_mensal.pop('mai') # Remove o valor vinculado a chave do dicionário e o retorna
print(lucro_mensal,type(lucro_mensal))
del lucro_mensal['abr']
print(lucro_mensal,type(lucro_mensal))

# Alguns métodos de dicionários
print("\nExemplo - copiando dicionário para outro dicionário\n")
dados = dict(temp = 27.5, hum = 0.74, pres = 0.98, wind = 4.8)
print(dados, type(dados))

print("\nDeep Copy:")
novo = dados.copy() # Deep Copy
print(novo, type(novo))
novo.update({'sun_rad':784})
print(dados, type(dados))
print(novo, type(novo))

print("\nShallow Copy:")
novo2 = dados #Shallow Copy
print(novo2, type(novo2))
novo2.update({'sun_rad':784})
print(dados, type(dados))
print(novo2, type(novo2))

print("\nExemplo - limpando dicionário\n")
dados. clear() # Excluindo todos os elementos do dicionário
print(dados, type(dados))

# Iterando em dicionários
print("\nExemplo - iterando em dicionários\n")
produtos ={1:'arroz', 2: 'feijão', 3: 'frango', 4:'batata', 5:'macarrão'}

print("A iteração padrão retorna as chaves:")
for codigo in produtos:
    print(codigo, end=' ')

print("\n\n Outra forma de iteração que retorna as chaves:")
for codigo in produtos.keys(): #Recomendado
    print(codigo, end=' ')
  
print("Para retornar o valor pode se utilizar:")
for codigo in produtos:
    print(produtos[codigo], end=' ')
  
print("\n\nPara retornar os valores pode se utilizar o método values():")    
for produto in produtos.values(): #Recomendado
    print(produto, end=' ')
 
print("\n\nPara retornar em tuplas os pares chave/valor utiliza-se o método items():")        
for i in produtos.items():
    print(i, end=' ')
    
print("\n\nE para desempacotamento:")      
for i, j in produtos.items():
    print(i, j)
    
    
