#9. Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if num2 > num1:
    print("O numero maior é: ",num2)
elif num1 > num2:
    print("O numero maior é: ",num1)    
else:
    print("Dado invalido")