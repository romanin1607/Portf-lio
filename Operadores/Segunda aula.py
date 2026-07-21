salario = int(input("Qual seu salario? "))
aumento = salario * 0.15
print("seu salario novo será de {}".format(salario + aumento))

# ================================================================================== #

n1 = int(input("Escolha um numero:"))
print("O antecessor do numero escolhido é {} \n e o sucessor é {}".format(n1 - 1, n1 + 1))

# ================================================================================== #

n2 = int(input("escolha um numero: "))
print("O dobro desse numero é {} , o triplo é {} e a raiz quadrada é {}".format(n2 * 2, n2 * 3, n2 ** 0.5))

# ================================================================================== #

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua segunda nota: "))
print("Sua media é {}".format((nota1 + nota2) / 2))

# ================================================================================== #

metros = int(input("Digite os metros: "))
cm = metros * 100
mm = metros * 1000

print("{} metros é igual a {} centrimetros e {} milimetros".format(metros, cm, mm))

# ================================================================================== #

reais = float(input("digite quantos reais tu tens: "))
dolares = reais * 3.27

print("Convertendo {} reais em dolares, são {} dolares".format(reais, dolares))

# ================================================================================== #

preço = float(input("Qual o preço? "))
desconto = 0.05 * preço
npreço = preço - desconto
print("o novo preço será de {} reais".format(npreço))