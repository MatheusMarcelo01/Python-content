class Fila():                                       #Cria a classe fila e inicia a variável data
    def _init_(self):
        self.data = []

    def inserir(self, x):                           #Insere o valor x na fila data
        self.data.append(x)

    def remove(self):                               #remove o elemento mais a esquerda da fila
        if len(self.data) > 0:                      #se de fato houver um elemento na fila
            return self.data.pop(0)

    def top(self):                                  #mostra o próximo elemento que irá sair da fila
        if len(self.data) > 0:                      #se de fato houver um elemento na fila
            return self.data[0]

    def empty(self):                                #retorna 1 se a fila estiver vazia
        return not len(self.data) > 0               #ou 0 se a fila estiver com algum elemento

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Criando as filas
f = Fila()  #Fila comum
p = Fila()  #Fila prioritária

pessoas = 0
Max = 5         #Número máximo de pessoas atendidas

#Coleta as pessoas que chegam na fila
while pessoas != Max:
    idade = int(input("Informe sua idade: "))
    nome = str(input("Informe seu nome: "))
    if idade > 60:
        p.inserir(nome)
    else:
        f.inserir(nome)
    pessoas = pessoas + 1

#Chama as pessoas da fila conforme a ordem de chegada
aux = 0
while p.empty() != 1 or f.empty() != 1:
    if aux < 2:
        if p.empty() != 1:
            print(p.remove())
        aux = aux + 1
    else:
        print(f.remove())
        aux = 0
