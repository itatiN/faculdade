# 13. Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso.
#  Caso o usuário digite um número que não esteja neste intervalo, exibir mensagem: número inválido.

num = int(input("Digite um numero de 1 a 5:"))

if num == 1:
    print("Um")
elif num == 2:
    print("Dois")
elif num == 3:
    print("Tres")
elif num == 4:
    print("Quatro")
elif num == 5:
    print("Cinco")
else:
    print("Nao esta no intervalo de 1 a 5")