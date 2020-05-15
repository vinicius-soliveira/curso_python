""" Resumo da aula de condicionais"""

idade = int(input("Digite a sua idade: "))

if idade<=12:
    print("Você é uma criança")
elif 12 < idade <17:
    print("Você é um adolescente")
elif 17<=idade<21:
    print("Você é um jovem")
elif 21<=idade<65:
    print("Você é um adulto")
elif idade >=65:
    print("Você é um idoso")
      
      
ativo = True
logado = False

if ativo:
    print("Bem vindo usuário")
else:
    print("Verifique seus dados")
    
if  not logado: # Se for falso a condição é valida
    print("Você precisa logar a sua conta")
else:
    print("Bem vindo!")
    
nome = 'Vinicius'

if 'i' in nome:
    print ("Existe a letra i no seu nome")
else:
    print("Não existe a letra i em seu nome")
    
    
 # Operador ternário

cadastrado = True
msg = 'Usuário cadastrado' if cadastrado else 'Usuário não cadastrado' 
    
usuário = input('Qual o seu nome? ')

print(nome or "Você não digitou nada!")  