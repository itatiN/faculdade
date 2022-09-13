#2. Ler uma temperatura em graus Celsius e apresentá-la convertida em
#graus Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F
#a temperatura em Fahrenheit e C a temperatura em Celsius

temp = int(input("Digite sua temperatura em graus Celsius: "))
convert = (9*temp+160)/5
print("A temperatura em Fahrenheit é de :",convert)