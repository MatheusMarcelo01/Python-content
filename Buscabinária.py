import random
l= random.sample(range(100), 20) #vamos importar um lista aleatoria, contendo uma popolução de 0 a 100, com 20 elementos
l.sort() # para ordenar os elementos
print(l)

def busca_binaria(l, x, inicio, fim): #x é o número a ser buscado na lista
    meio =(inicio+fim) // 2

    if x == l[meio]:
        return meio #o número esta no meio
    if x< l[meio]:
        return busca_binaria (l,x, inicio, meio -1)

    if x > l[meio]:
        return busca_binaria(l,x, meio +1, fim)

#No terminal digitamos:

busca_binaria(l, 92, 0,19) #l é a lista em si, o 92 é a variavel (número que queremos buscar), 0 é o inicio e 19 o fim da lista.
