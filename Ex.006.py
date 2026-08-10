#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
n = int(input("Escolha um número: "))
d = n*2
t = n*3
r = n**(1/2)
print("O dobro de {} é {} e o triplo é {} e a raiz quadrada é igual a: {}" .format(n,d,t,r))