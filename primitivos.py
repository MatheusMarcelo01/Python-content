n1=eval(input('digite '))
n2=eval(input('digite dnv'))
s=n1+n2
# para este cód ficar mais simples: print('a soma de', n1,'+',n2,'é {}!:'.format(s)), pode-se fazer assim:
print('a soma de {} + {} é {}'.format(n1, n2, s))

#identificando primitivos:
a=(input('digite algo'))
print('o que você digitou é um elemento de tipo:', type(a))
print ('ele é um número?', a.isnumeric())
print('ele é alfanumerico?', a.isalnum())
print('ele é um número decimal?', a.isdecimal())
print('ele é escrito em letras minusculos?', a.islower(), 'é escrito em letras maiusculas?', a.islower())
