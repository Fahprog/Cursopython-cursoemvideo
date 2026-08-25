#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input("Primeiro nome: "))
a2 = str(input("Segundo nome: "))
a3 = str(input("Terceiro nome: "))
a = str(input("Quarto nome: "))

l = [a1, a2, a3, a]
s = random.choice(l)
s1 = random.choice(l)
s2 = random.choice(l)
s3 = random.choice(l)

print("O resultado do sorteio é: {}, {}, {}, {}." .format(s, s1, s2 ,s3))