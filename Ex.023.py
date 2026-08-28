#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Mostre unidade, dezena centema e milhar
n = (input("Escolha um número de 0 a 9999: "))
len(n)
n1 =n[3] 
n2 = n[2]
n3 = n[1]
n4 = n[0]

print("Unidade: {}. \nDezena: {}. \nCentena: {}. \nMilhar: {}" .format(n1,n2,n3,n4))