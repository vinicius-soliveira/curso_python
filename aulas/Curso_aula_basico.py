nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso/(altura**2)

print(nome, type(nome))
print(idade, type (idade))
print(altura, type(altura))
print("Maior de idade?", idade>=18, type(idade>=18))

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}' .format(nome, idade, imc)) 

# Trocar valores de variáveis em python

x = 10
y = 'bola'

x, y = y, x

# Métodos de strings
