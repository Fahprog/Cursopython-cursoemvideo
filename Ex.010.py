#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares elapode comprar
#Cotação atual do dólar 5,11

r = float(input("Começo de mês, quantos reais ainda em em carteira?"))
d = r * 0.1958
print("Atualmente com a quantidade de dinhero que você tem, {}reais, você pode comprar exatos {:.2f}dolares." .format(r,(d)))

