#1. Ler dois valores para as variáveis A e B, e efetuar as trocas 
# dos valores de forma que a variável A passe a possuir o valor da variável B e a 
# variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

a = input("Digite seu valor para a: ")
b = input("Digite seu valor para b: ")
holderA = a
holderB = b
a = holderB
b = holderA
print("Seu valor de a",holderA," seu valor de b ",holderB)
print("Seu valor de a trocado com b",a," seu valor de b trocado com a ",b)