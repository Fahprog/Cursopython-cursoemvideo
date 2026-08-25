#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
print("Digite o nome dos alunos que participarão do sorteio!")
pn = str(input("Primeiro nome: "))
sn = str(input("Segundo nome: "))
tn = str(input("Terceiro nome: "))
qn = str(input("Quarto nome: "))

ns = [pn, sn, tn, qn]
s = random.choice(ns)
print("O nome sorteado foi: {}" .format(s))


