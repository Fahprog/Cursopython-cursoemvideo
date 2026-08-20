#xercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input("Digite o número de dias que o carro foi alugado: "))
km = float(input("Digite o número de kms rodados: "))
pp = d * 60 + km * 0.15
print ("Seu saldo devedor é de: R${}" .format(pp))

       