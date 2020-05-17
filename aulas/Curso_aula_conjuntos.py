'''
Conjuntos, da mesma forma que na matemática são sequências de elementos.
Em Python os conjuntos não possuem valores duplicados, não possuem valores
duplicados, os conjuntos não são acessados via índice

Conjuntos são bons para armazenamento de elementos sem que a ordenação seja
necessaria.

Os conjuntos são referenciados por chaves:{}

'''
# Criando um conjunto
print("\nExemplo - criando conjuntos")
s = set({1,2,3,4,2,3,4,5})
print(s,type(s))
s = {1,2,3,4,2,3,4,5}
print(s,type(s))
s = {1, 'teste', True, 27.54, (1,2,3)} # Um conjunto suporta diferentes tipos de dados
print(s,type(s))

# Adicionando elementos a um conjunto
print("\nExemplo - adicionando elementos em conjuntos")
conj = {1,3,5,7,9}
print(conj,type(conj))
conj.add(11)
print(conj,type(conj))
conj.add(1) #ignora a inserção de um termo repetido
print(conj,type(conj))

# Removendo elementos de um conjunto
print("\nExemplo - removendo elementos em conjuntos")
conj = {1,3,5,7,9}
print(conj,type(conj))
conj.remove(1) # o argumento é o elemento
print(conj,type(conj))
conj.discard(3)
print(conj,type(conj))
conj.clear() #remover todos os elementos
print(conj,type(conj))

# Copiando um conjunto para outro
print("\nExemplo - copiando um conjunto para outro")
original = {1,2,3,4,5,6}
print('\nDeep Copy')
print(original)
novo = original.copy()
novo.add(7)
print(novo)
print(original)

print('\nShallow Copy')
print(original)
novo = original
novo.add(7)
print(novo)
print(original)

# Métodos matemáticos de Conjuntos
print("\nExemplo - métodos matemáticos de conjuntos")
mult_3 = {0,3,6,9,12,15,18,21,24,27,30}
mult_5 = {0,5,10,15,20,25,30,35,40,45,50}
print(mult_3)
print(mult_5)

print('\nUnion')
mult_3e5 = mult_3.union(mult_5)
print(mult_3e5)
mult_3e5 = mult_3 |  mult_5
print(mult_3e5)

print('\nIntersection')
mult_15 = mult_3.intersection(mult_5)
print(mult_15)
mult_15 = mult_3 &  mult_5
print(mult_15)

print('\nDifference')
mult_3n5 = mult_3.difference(mult_5)
print(mult_3n5)

# Operações matemáticas em conjuntos numéricos
print("\nExemplo - operações matemáticas de conjuntos\n")
conjunto = {10,4,2,8,9,11,18,21,0,1,3,45}
print(f'A soma dos elementos do conjunto é {sum(conjunto)}')
print(f'O maior elemento do conjunto é {max(conjunto)}')
print(f'O menor elemento do conjunto é {min(conjunto)}')
print(f'O conjunto possui {len(conjunto)} elementos')



