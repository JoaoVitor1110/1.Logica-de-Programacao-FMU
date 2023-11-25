#1. Elabore um algoritmo que calcule a área de um triângulo a partir da entrada de dados feita por um usuário.
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

soma_total = 0
media_total = 0
contador = 0

for letra in range(ord('A'), ord('U')):
    numero = int(input(f"Digite o número correspondente à letra {chr(letra)}: "))
    
    soma_total += numero
    contador += 1
    
    if contador % 5 == 0:
        media_grupo = soma_total / 5
        media_total += media_grupo
        print(f"Média do grupo: {media_grupo}")
        
        soma_total = 0
        contador = 0

media_final = media_total / 4
print(f"Média final entre os grupos: {media_final}")


#5. Escreva um algoritmo que, após a leitura do salário bruto de um funcionário, calcule o salário líquido a receber descontando o IRRF de acordo com a tabela de referência abaixo:

sal = float(input("Escreva seu salario bruto R$"))
if sal <= 1710.78:
    print("Isento de IRRF") 
elif sal >= 1710.79 and sal <= 2563.90:
    print("Aliquota de Desconto: 7,5%")
    print(f"Seu salario com desconto será: R${sal*0.925}")    
elif sal >= 2563.91 and sal <= 3418.59:
    print("Aliquota de Desconto: 15%")
    print(f"Seu salario com desconto será: R${sal*0.85}")  
elif sal >= 3418.60 and sal <= 4271.59:
    print("Aliquota de Desconto: 22,5%")
    print(f"Seu salario com desconto será: R${sal*0.775}")  
else:
    print("Aliquota de Desconto: 27,5%")
    print(f"Seu salario com desconto será: R${sal*0.725}")

#6. Elabore um algoritmo que leia 3 números inteiros e aponte qual deles é o maior e qual deles é o menor.
n1 = int(input("Digite um numero: "))
maior = n1
menor = n1
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite o ultimo numero: "))
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1:
    maior = n3

print(f"O menor valor foi {menor} e o maior valor foi {maior}")

#7. Escreva um algoritmo que faça a leitura das idades, peso e altura para 10 pessoas e mostre ao final a média de todas as informações separadamente, ou seja, idade, peso e altura.

num_pessoas = 10
soma_idade = 0
soma_peso = 0
soma_altura = 0

for c in range(1, num_pessoas + 1):
    print(f"---Cadastro nº{c}---")

    idade = float(input("Digite a idade: "))
    soma_idade += idade

    peso = float(input("Digite o peso: "))
    soma_peso += peso

    altura = float(input("Digite a altura: "))
    soma_altura += altura

media_idade = soma_idade / num_pessoas
media_peso = soma_peso / num_pessoas
media_altura = soma_altura / num_pessoas

print("A média das idades é de: %.2f" % media_idade)
print("A média dos pesos é de: %.2f" % media_peso)
print("A média das alturas é de: %.2f" % media_altura) 

#8. Escreva um algoritmo que, a partir da leitura de 5 números inteiros, calcule a média aritmética entre eles, mostrando o resultado ao final.
numeros = 5
soma = 0
for c in range(1, numeros + 1):
    num = int(input("Digite um numero: "))
    soma += num

media = soma / numeros
print(f"A média dos numeros digitados é de {media:.2f}")    

#9. Elabore um algoritmo que calcule a velocidade média de um carro tendo como entradas o espaço percorrido e o tempo levado durante o percurso. (Se não lembrar a fórmula, consulte algum livro de física).

distancia = float(input("Digite a distancia (em Km): "))
tempo = float(input("Digite o tempo percorrido (em horas): "))

velocidade = distancia/tempo
print(f"A velocidade média é de {velocidade:.2f} km/h")
