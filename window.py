#Teste com tkinter
from tkinter import Tk,Label, PhotoImage, TOP, BOTTOM
''' tkinter que serão usadas para criar a interface gráfica (GUI).
Tk é a classe principal que representa a janela da GUI, 
Label é usado para exibir texto ou imagens, 
PhotoImage é usado para exibir imagens
TOP e BOTTOM são constantes que representam a posição dos widgets. '''

root = Tk()

photo= PhotoImage (file='walle.gif').subsample(3) #.subsample é para redimensionar.
image= Label(master=root, image=photo, width=300, height=180) #width e height é medida da janela em si.
image.pack(side=TOP) #posição da imagem.

text= Label(master=root, font=("Courier",20), text='hello Earth, my name is Walle!')
text.pack(side=BOTTOM)

root.mainloop()
