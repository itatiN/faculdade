#11. Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre.
#  Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7),
#  Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).

nome = str(input("Qual seu nome? : "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1+nota2+nota3)/3

if media >=7:
    print("Aprovado")
elif media>5 and media<7:
    print("Recuperação")
elif media <=5:
    print("Reprovado")
else:
    print("Dados Incorretos")