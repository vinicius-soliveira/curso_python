from random import randint
cpf_raw = str(randint(100000000, 999999999))

soma_1, soma_2 = 0, 0
             
for indice, digito in enumerate(cpf_raw):
    
    soma_1 += int(digito)*(10-indice)
    soma_2 += int(digito)*(11-indice)
    
digito_1 = 11 - (soma_1%11)
digito_1 = 0 if digito_1 > 9 else digito_1 
soma_2 += digito_1*2
digito_2 = 11 - (soma_2%11)

print(f"{cpf_raw[0:3]}.{cpf_raw[3:6]}.{cpf_raw[6:9]}-{digito_1}{digito_2} é um CPF válido")