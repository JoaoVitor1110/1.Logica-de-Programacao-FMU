#1- Faça um programa em Python que imprima os números pares entre 0 e 100
contador = 0
while contador <101:
    print(contador)
    contador += 2

#2- Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1 e de 52 a 100 de 2 em 2.

ateCinquenta = 1
ateCem = 52

for ateCinquenta in range(1, 53):
    print(ateCinquenta)

for ateCem in range (52, 101, 2):
    print(ateCem)

#3-  Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:
n = int(input("Digite um valor inteiro e positivo: "))
S = 0
for i in range(1, n + 1):
    S += 1/i
    print("A soma S é:", S)

#4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar.

quantidade_positivos = 0
quantidade_negativos = 0
menor_valor = None

n = int(input("Digite a quantidade de valores que deseja inserir: "))
i = 0
while i < n:
    valor = float(input(f"Digite o {i + 1}º valor: "))
    quantidade_positivos += (valor > 0)
    quantidade_negativos += (valor < 0)
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor
        
    i += 1
    
print(f"Quantidade de valores positivos: {quantidade_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")
print(f"O menor valor é: {menor_valor}")

#5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens separadamente. Utilize o comando de repetição que desejar

altura_total_homens = 0
altura_total_mulheres = 0
contagem_homens = 0
contagem_mulheres = 0

while True:
    sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino, ou X para sair): ")
    
    if sexo.upper() == 'X':
        break

    altura = float(input("Digite a altura da pessoa em metros: "))

    if sexo.upper() == 'M':
        altura_total_homens += altura
        contagem_homens += 1
    elif sexo.upper() == 'F':
        altura_total_mulheres += altura
        contagem_mulheres += 1

altura_media_homens = altura_total_homens / contagem_homens if contagem_homens > 0 else 0
altura_media_mulheres = altura_total_mulheres / contagem_mulheres if contagem_mulheres > 0 else 0

print(f"Altura média dos homens: {altura_media_homens:.2f} metros")
print(f"Altura média das mulheres: {altura_media_mulheres:.2f} metros")
