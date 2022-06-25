from tkinter import Tk, Label, RAISED
raiz =  Tk()
labels   = [['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
            ['*','0','#']]

for r in range (4): #para cada linha em r=0,1,2,3
    for c in range(3):  #para cada coluna em c=0,1,2,3
        #cria label para linha r e coluna c
         label = Label(raiz,
                  relief=RAISED,    #borda elevada
                  padx=20,          #torna o label mais largo
                  pady=20,
                  font=('courier',25), 
                  text=labels[r][c])  #texto do label
    # coloca label na linha r e coluna c

         label.grid(row=r, column=c)

raiz.mainloop()
