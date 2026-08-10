#Escreva um programa que leia um valor em metros e o exiba convertido em cm e milimetros
n = int(input("Digite o n° de metros que você queira converter em cm e/ou milimetros: " ))
c = n*100
m = n*1000
print(" {} m, tem exatos {}cm ou {}mm".format(n,c,m))
