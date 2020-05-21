
def detecta_duplicacao(*args):
    pos = []
    args = list(*args)
    for i in range(0,12,1):
        duple = False
        aux = args[i]
        for j in range(0,10,1):
            for k in range(j+1,10,1):             
                if aux[j] == aux[k]:
                    pos.insert(i,aux[k])
                    duple = True
                    break
            if duple: break
        if not duple:
            pos.insert(i, -1)
             
    return pos
      

def detecta_primeira_repeticao(*args):
    value = []
    args = list(*args)
    for i in range(0,12,1):
        duple = False
        aux = args[i]
        pos = 10
        x=-1
        for j in range(0,10,1):
            for k in range(j+1,10,1):                  
                if aux[j] == aux[k] and k < pos:
                    x= aux[k]
                    pos = k
                    duple = True
        if duple:
            value.insert(i, x)
        else:
            value.insert(i, -1)
             
    return value 
      
def encontra_primeira_repeticao(lista):
    numeros_checados = set()
    primeiro_repetido = -1
    for i in lista:
        if i in numeros_checados:
            primeiro_repetido = i
            break
        numeros_checados.add(i)
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

#print(len(lista_de_listas_de_inteiros))
print(detecta_duplicacao(lista_de_listas_de_inteiros))
print(detecta_primeira_repeticao(lista_de_listas_de_inteiros))
