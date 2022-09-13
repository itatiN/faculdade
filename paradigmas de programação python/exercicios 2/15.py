nome = str(input("Qual seu nome? "))
sexo = int(input("Digite 1 para masculino e 2 para feminino"))
idade = int(input("Digite sua idade: "))
salario = float(input("Qual seu salario? "))

if sexo == 1:
  if idade < 30:
    salario = salario + 50
  else:
    salario = salario + 100

if sexo == 2:
  if idade < 30:
    salario = salario + 80
  else:
    salario = salario + 200

print(nome,"seu salario é: ",salario)