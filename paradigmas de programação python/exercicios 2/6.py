#6. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda.
# Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

costprice = int(input("Qual o preço de custo? "))
convert = int(input("Qual o lucro liquido do objeto? "))
marketprice = costprice + convert
print("O valor de venda é de:",marketprice)