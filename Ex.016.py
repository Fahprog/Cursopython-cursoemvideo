#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#from math import trunc
#ni = float(input("Digite um número com decimais: "))
#print("A porção inteira de {}, é: {} " .format(ni, trunc(ni)))

ni = float(input("Digite um número com casas decimais: "))
print("A porção inteira de {}, é: {:.0f}. " .format(ni, ni))


