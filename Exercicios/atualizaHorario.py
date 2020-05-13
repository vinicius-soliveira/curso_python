hora_inicial = int(input("Digite a hora inicial do experimento: "))
minuto_inicial = int(input("Digite o minuto inicial do experimento: "))
segundo_inicial = int(input("Digite o segundo inicial do experimento: "))

duracao = int(input("Digite o duracao do experimento: "))

segundo_final = (segundo_inicial+duracao) % 60
minuto_final = (minuto_inicial + (segundo_inicial+duracao) // 60)%60
hora_final = (hora_inicial + (minuto_inicial + (segundo_inicial+duracao) // 60)//60)%24

print(f"O experimento iniciou às {hora_inicial}h{minuto_inicial}min{segundo_inicial}s")
print(f"O experimento terminou às {hora_final}h{minuto_final}min{segundo_final}s")


