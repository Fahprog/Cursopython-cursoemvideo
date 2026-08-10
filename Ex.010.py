#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares elapode comprar
#Cotação atual do dólar 5,11
#Primeiro contando dolar com cambio
r = float(input("Começo de mês, quantos reais ainda em em carteira?"))
d = r * 0.1958
print("Atualmente com a quantidade de dinhero que você tem, {}reais, você pode comprar exatos {:.2f}dolares." .format(r,(d)))

#Outra forma e mais correta de fazer é
R = float(input("Diga-me quantos reais tens em carteira?: "))
D = r / 5.11
print("Com esse valor {0} reais, você pode comprar {1}dólares." .format(R,D))