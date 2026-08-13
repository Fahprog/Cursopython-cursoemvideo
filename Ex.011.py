#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
#FRaça um algoritmo que leia o preço de um produto e mostre o novo preço com 5%de desconto
l = float(input("Digite aqui a largura de sua parede: "))
a = float(input("Digite aqui a altura de sua parede: "))
ar = l * a
t = ar / 2

print("A área de sua parede é de: {:.2f}m², a quantidade de tinta necessaria é de {:.2f} litros." .format(ar,t))
