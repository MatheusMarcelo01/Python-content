import json

def substituir_nome_no_json(arquivo_json, nome_antigo, nome_novo):
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    def substituir_recursivamente(dados):
        if isinstance(dados, dict):
            for chave, valor in dados.items():
                dados[chave] = substituir_recursivamente(valor)
        elif isinstance(dados, list):
            for i in range(len(dados)):
                dados[i] = substituir_recursivamente(dados[i])
        elif isinstance(dados, str):
            return dados.replace(nome_antigo, nome_novo)
        return dados

    dados_modificados = substituir_recursivamente(dados)

    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(dados_modificados, f, indent=4, ensure_ascii=False)

arquivo_json = 'db.json'

#Substitui
substituir_nome_no_json(arquivo_json, 'Matheus Marcelo', 'Marcelo')

print("Substituição realizada com sucesso!")
