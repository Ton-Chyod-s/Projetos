import json

def criar():
    dados = {
    'nome': 'um_nome',
    'profissao': 'Desenvolvedor de sistemas'
    }
    with open('Novo.json','w') as json_file:
        json.dump(dados, json_file, indent=4) #json formatado por linha 
        
criar