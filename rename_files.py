import os

diretorio_atual = os.getcwd()

extensoes_imagem = ['.jpg', '.jpeg', '.png', '.gif']

contador = 1

for arquivo in os.listdir(diretorio_atual):
    if any(arquivo.lower().endswith(ext) for ext in extensoes_imagem):
        novo_nome = f'Casa_{contador}{os.path.splitext(arquivo)[1]}'
        
        caminho_antigo = os.path.join(diretorio_atual, arquivo)
        caminho_novo = os.path.join(diretorio_atual, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        
        contador += 1

print("Renomeação concluída!")
