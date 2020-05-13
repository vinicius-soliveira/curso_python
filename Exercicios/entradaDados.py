print('Qual o seu nome? ', end = ' ')
nome = input()

#print('Seja Bem vindo {}'.format(nome))
print(f'Seja bem vindo {nome}')
print('Qual a sua idade?', end = ' ')
idade = input()

print(f'O {nome} tem {idade} anos')
print(f'O {nome} nasceu em {2020 - int(idade)}')
