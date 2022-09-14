#5. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações
# sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

print("\t\t\tMAMAO COM AÇUCAR\t\t\t")
valor = int(input(" Sua compra foi de ? : "))
mode = int(input(" Deseja pagar usando Cartao de Credito(1) ou Debito(2): "))
if mode==1:
    quant = int(input(" Deseja pagar em quantas prestações(MAX 5) : "))
    print(" O valor de suas prestações sera de :",valor/quant)
if mode==2:
    print(" Sua compra foi debitada no valor de:",valor)   