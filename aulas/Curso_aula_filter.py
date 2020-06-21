'''
Filter 

Filter é uma função integrada do Python e é utilizada para filtrar
dados de uma determinada coleção.

'''
############### Utilizando filter ########################
print(" ")
print("Exemplo: utilizando filter")
print(" ")

valores = 1,2,3,4,5,6,7,8
media = sum(valores)/len(valores)
print(media)
acima_da_media =filter(lambda x: x > media, valores)
print(list(acima_da_media))

############ Exemplo: remoção de dados faltantes ##########
print(" ")
print("Exemplo: remoção de dados faltantes")
print(" ")
estados = ['', 'Acre', '', 'Ceará', 'Goiás', '','', 'Pará']
print(estados)
estado = filter(None, estados)
print(list(estado))

############ Exemplo mais complexo ########################
print(" ")
print("Exemplo mais complexo")
print(" ")

inscritos = [
    {'nome': 'Adam', 'idade': 25, 'cidade': 'São Paulo'},
    {'nome': 'Laura', 'idade': 17, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Carlos', 'idade': 32, 'cidade': 'Vitória'},
    {'nome': 'João', 'idade': 14, 'cidade': 'Recife'},
    {'nome': 'Rebeca', 'idade': 16, 'cidade': 'Curitiba'},
    {'nome': 'Tiago', 'idade': 21, 'cidade': 'Fortaleza'},
]
print(inscritos)
# Só aceita os maiores de idade
selecionados =  filter(lambda dados: dados['idade'] >= 18, inscritos)
print(list(selecionados))