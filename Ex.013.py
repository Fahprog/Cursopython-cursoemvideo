#Crie um programa que dê 15% de aumento no salário

s = float(input("Qual o valor do seu salário atualmente?: "))
a = s * 0.15 + s
print("Com um aumento de 15% no seu sálario atual: R${}, você passará a receber o valor de R${:.2f}" .format(s,a))
