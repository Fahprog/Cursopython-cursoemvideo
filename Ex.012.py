#Faça um algoritmo que leia o preço de um produto e mostre o novo preço com 5% de desconto
v = float(input("Digite o valor do seu produto: "))
d = v * 0.05
r = v - d

print("Com o desconto de 5%, o seu produto fica no valor de: {:.2f}." .format(r))