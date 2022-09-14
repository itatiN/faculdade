#12. Faça um algoritmo que leia dois números e identifique se são iguais ou diferentes.
# Caso eles sejam iguais imprima uma mensagem dizendo que eles são iguais.
# Caso sejam diferentes, informe qual número é o maior, e uma mensagem que são diferentes.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if num1 == num2:
    print("Os seus numeros sao iguais")
elif num1>num2:
    print("Os seus numeros nao sao iguais,e o maior é",num1)
elif num2>num1:
    print("Os seus numeros nao sao iguais,e o maior é",num2)
else:
    print("Dados invalidos")