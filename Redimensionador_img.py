from PIL import Image

def redimensionar_imagem(caminho_imagem, largura, altura):
    imagem = Image.open(caminho_imagem)
    imagem_redimensionada = imagem.resize((largura, altura))
    caminho_saida = f'redimensionada_{largura}x{altura}.png'
    imagem_redimensionada.save(caminho_saida)
    
    print(f'Imagem redimensionada salva como: {caminho_saida}')

def main():
    caminho_imagem = input("Digite o caminho da imagem que deseja redimensionar (pwd): ")
    tamanho = input("Qual o tamanho? (ex: 28x28): ")
    
    try:
        largura, altura = map(int, tamanho.split('x'))
        redimensionar_imagem(caminho_imagem, largura, altura)
    except ValueError:
        print("Formato de tamanho inválido. Use o formato LARGURAxALTURA (ex: 28x28).")

if __name__ == "__main__":
    main()
