#3. Elaborar um algoritmo que efetue a apresentação do valor da conversão
# em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar
# o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

dol = int(input("Quantos dolares voce tem? "))
valorconvert = int(input("Qual o valor da cotação do dolar? "))
convert = dol*valorconvert
print("Voce tem",convert,"reais")