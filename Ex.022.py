#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

n = input("Digite seu nome completo: ")
N = (n.upper())
nm = (n.lower())
d = n.split()
se = "".join(d)
print("Nome em maiúsculas: {}, \nNome em minúsculas: {}. " .format(N, nm))
print("N° de letras: ",len(se))
print("N° de letras no 1° nome: ",len(d[0]))
