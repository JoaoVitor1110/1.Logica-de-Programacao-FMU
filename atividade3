#1-Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão: volume =h/3*(Bmaior**2 +  Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5) 

h = float(input("Qual a altura do tronco: "))
bMenor = float(input("Digite o valor da base menor: "))
bMaior = float(input("Digite o valor da base maior: "))
volume = h/3*(bMaior**2 +  bMenor**2 + (bMaior**2 * bMenor**2)**0.5)
print(f"O valor do volume do tronco é de {volume}")

#2- Crie um programa em Python que solicite o valor em horas para o usuário, calcule e mostre o valor em minutos, sabendo que 1 hora tem 60 minutos.

hora = int(input("Que horas são: "))
min = hora*60
print(f"Se são {hora} horas, se passaram {min} minutos")

#3- Crie um programa em Python que solicite ao usuário a sua idade expressa em anos, meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

anos = int(input("Quantos anos você tem: "))
meses = anos*30
dias = anos*365

print(f"Você tem {anos} anos, se passaram {meses} meses e {dias} dias.")

#4- Escreva um programa em Python para calcular o valor de uma prestação em atraso (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que: prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

valorPrestacao = float(input("Qual o valor da prestação atrasada: "))
multa = 1.02
qtdeDias = int(input("Quantos dias você atrasou a prestação: "))
prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
print(f"Sua prestação de atraso será de R${prestacao}")

#5- Faça uma programa em Python que peça do usuário um valor em graus para um ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.

import math

angulo = float(input("Quantos graus tem o angulo?: "))
angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)
