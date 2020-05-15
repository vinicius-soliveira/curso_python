'''
Um CPF é formado por 11 dígitos, em que os 9 primeiros são aleatórios e os dois ultimos são gerados a partir dos 9 primeiros(cpf_raw) .
Para gerar os ultimos digitos obtem a soma dos produtos 10*1ºdigito, 9*2ºdigito...2*9ºdigito 
 

'''

while True:
    cpf = input("Digite o seu CPF(apenas números): ")

    if not cpf.isnumeric():
        print("Digite apenas números!")
        continue
          
    soma_1, soma_2 = 0, 0
             
    for indice, digito in enumerate(cpf):
        soma_1 += int(digito)*(10-indice)
        soma_2 += int(digito)*(11-indice)
        if indice == 8:
            break
    
    digito_1 = 11 - (soma_1%11)
    digito_1 = 0 if digito_1 > 9 else digito_1 
    soma_2 += digito_1*2
    digito_2 = 11 - (soma_2%11)
    
    if digito_1 == int(cpf[9]) and digito_2 == int(cpf[10]):
        print("Seu CPF é válido!!")
    else:
        print("Seu CPF é inválido!!")
        
    if not input("Digite qualquer tecla para validar outro CPF ") :
        break
     