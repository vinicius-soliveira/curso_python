perguntas = {
    'Pergunta 1':{
        'pergunta': 'Qual a capital do Brasil?',
        'alternativas': {
            'a': 'São Paulo',
            'b': 'Rio de Janeiro',
            'c': 'Brasília',
            'd': 'Ceará'},
            'resposta': 'c',   
    },
    'Pergunta 2':{
        'pergunta': 'Qual das opções abaixo não é uma fruta?',
        'alternativas': {
            'a': 'Caju',
            'b': 'Castanha',
            'c': 'Tomate',
            'd': 'Banana'},
            'resposta': 'a',
    },
    'Pergunta 3':{
        'pergunta': 'Qual o nome da moeda americana?',
        'alternativas': {
            'a': 'Ouro',
            'b': 'Real',
            'c': 'Euro',
            'd': 'Dólar'},
            'resposta': 'd',
    },
    #ADICIONE MAIS PERGUNTAS AQUI           
}

acertos = 0
questoes = len(perguntas)

for qst_k, qst_v in perguntas.items():
    print(f"\n{qst_k}: {qst_v['pergunta']}")
        
    for ans_k, ans_v in qst_v['alternativas'].items():
        print(f'{ans_k}): {ans_v}')
           
    resposta_usuario = input("Escolha a alternativa CORRETA: ")
    
    if resposta_usuario == qst_v['resposta']:
        acertos+=1
    else:
        pass    

nota = acertos / questoes * 10
print(f"\nVocê acertou {acertos} perguntas. \nSua nota foi {nota:.2f}\n")


    
    
     