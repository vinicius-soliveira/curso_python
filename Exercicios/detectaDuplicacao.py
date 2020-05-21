
'''
Algoritmo praa encontrar valores repetidos em uma lista:
Cria-se uma lista inicialmente vazia
A cada iteração adicona-se um valor da lista em verificação para a lista inicialmente vazia
Para detectar a repetição verifica-se antes de adicionar o valor a lista se este já existe na lista
Caso não, a busca continua até o fim da lista e a função retorna -1, caso sim a função retorna o numero repetido encontrado
'''

def encontra_primeira_repeticao(lista):
    numeros_checados = list()
    primeiro_repetido = -1
    for i in lista:
        if i in numeros_checados:
            primeiro_repetido = i
            break
        numeros_checados.append(i)
    return primeiro_repetido        
         
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeira_repeticao(lista_de_inteiros))