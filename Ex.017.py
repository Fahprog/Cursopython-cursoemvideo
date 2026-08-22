#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
c1 = float(input("Digite aqui o cateto oposto: "))
c2 = float(input("Digite aqui o cateto adjascente: "))
h = sqrt((c1**2) + (c2**2))
print("A hipotenusa é: {:.2f}." .format(h))