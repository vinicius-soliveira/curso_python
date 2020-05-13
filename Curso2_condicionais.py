""" Resumo da aula de condicionais"""

idade = int(input("Digite a sua idade: "))

if idade<=12:
    print("Você é uma criança")
elif idade > 12 and idade < 17:
    print("Você é um adolescente")
elif idade >= 17 and idade < 21:
    print("Você é um jovem")
elif idade >= 21 and idade < 65:
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
    
print("Mentira GitHub é um amorzinho")    