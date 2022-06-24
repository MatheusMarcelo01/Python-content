from tkinter import Tk,Label, PhotoImage, TOP, BOTTOM

root = Tk()

photo= PhotoImage (file='walle.gif').subsample(3) #.subsample é para redimensionar.
image= Label(master=root, image=photo, width=300, height=180) #width e height é medida da janela em si.
image.pack(side=TOP) #posição da imagem.

text= Label(master=root, font=("Courier",20), text='hello Earth, my name is Walle!')
text.pack(side=BOTTOM)

root.mainloop()
