#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input("Digite aqui o ângulo, apenas os números. \n Ex: 90. :"))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print("O Valor do seno é: {:.2f}, cosseno é: {:.2f} e a tangente é: {:.2f}" .format(s, c, t))

      