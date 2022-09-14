#8. Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 10.

num = int(input("Digite um numero: "))
if num>10:
    print("O numero é maior que dez")
elif num==10:
    print("O numero é dez")
else:
    print("O numero não é maior que dez")