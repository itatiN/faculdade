#4. Faça um algoritmo que receba um valor que foi depositado e exiba
#  o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.

valor = float(input("Digite o valor que deseja depositar: "))
convert = valor + valor**0.7
print("O valor com o juros mensal sera de",convert)