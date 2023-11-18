"""#1. Elabore um algoritmo que calcule a área de um triângulo a partir da entrada de dados feita por um usuário.
base = float(input("Digite o valor da base: "))
alt = float(input("Digite o valor da altura: "))
triangulo = (base*alt)/2
input(f"Com base nos dados, o triangulo será {triangulo}")

#2. Engendre um algoritmo que leia altura e peso de uma pessoa, calculando seu IMC e exibindo mensagens de classificação de acordo com a tabela do link abaixo:
kg = float(input("Digite o peso em kg: "))
alt = float(input("Digite a altura em metros: "))
imc = kg/(alt**2)
print("Seu IMC é: %.1f" %(imc))
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc >= 18.5 and imc < 24.9:
    print("Parabéns — você está em seu peso normal!")
elif imc >= 25 and imc < 29.9:
    print("Você está acima de seu peso (sobrepeso)")
elif imc >= 30 and imc < 34.9:
    print("Obesidade grau I")
elif imc >= 35 and imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")  

#3. Escreva um algoritmo que seja capaz de calcular o perímetro de uma circunferência.

import math
raio = float(input("Escreva o valor do raio: "))
circunferencia = 2 * math.pi * raio
print("A Circunferencia é de: %2.f" %(circunferencia))    

#4. Faça um algoritmo que calcule a média aritmética para 20 números inteiros lidos. Utilize como variáveis as letras do alfabeto (de A a T). A cada 5 números lidos, calcule a média daquele grupo. Ao final deverá ser calculada a média entre 4 grupos de números.

c1 = 1
grupo1 = []
while c1 < 5:
    grupo1 = int(print(f"Escreva o {c1}° numero do grupo 1"))
    c1 += 1"""

#5. Escreva um algoritmo que, após a leitura do salário bruto de um funcionário, calcule o salário líquido a receber descontando o IRRF de acordo com a tabela de referência abaixo:

sal = float(print("Escreva seu salario bruto R$"))
if sal <= 1710.78:
    print(Isento de IRRF) 
elif sal > 1710.78 or sal <=2563.91:
    print("Aliquota de Desconto: 7,5%")
    print(f"Seu salario com desconto será: R${sal*0.825}")    