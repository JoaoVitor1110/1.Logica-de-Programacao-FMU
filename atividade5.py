# 1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
 •  não-eleitor (abaixo de 16 anos)
 •  eleitor obrigatório (entre 18 e 65 anos)
 •  eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)

idade = int(input("Digite sua idade: "))
if idade < 16:
     print('Você não pode votar')
elif idade < 18 or idade > 65:
    print("Facultativo: Vota se quiser")
else:
    print('Obrigatório vá votar imediatamente')
=====================================================================================
#2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou zero); 
#a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta negativo); 
#e a mensagem "Não é equação do segundo grau", se o valor de a for igual a zero.

a = int(input('Digite um valor inteiro: '))
b = int(input('Digite o segundo valor inteiro: '))
c = int(input('Digite o ultimo valor inteiro: '))
if a == 0:
    print("Não é equação do segundo grau")
else:
    # Calcular o discriminante (delta)
    delta = b**2 - 4*a*c
    
    # Verificar se delta é positivo ou zero
    if delta >= 0:
        # Calcular as raízes
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        
        # Imprimir as raízes
        print("Raiz 1:", raiz1)
        print("Raiz 2:", raiz2)
    else:
        # Não há raízes reais
        print("Não há raízes reais")
=====================================================================================
#3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
 
#Crie uma programa que permita digitar o nome do produto e valor da compra, e imprimindo o nome do produto e o valor da venda.
# Valor de Compra            |  Valor de Venda
# valor < R$10,00            |  lucro de 70%
# R$10,00 <= valor < R$30,00 |  lucro de 50%
# R$30,00 <= valor < R$50,00 |  lucro de 40%
# valor > R$50,00            |  lucro de 30%

produto = input("Qual o nome do produto: ")
valor = float(input("Qual o valor do produto: R$"))
if valor < 10.0:
    print("Lucro de 70%:", valor*1.7)
elif valor <= 30.0: 
    print('Lucro de 50%:', valor*1.5)
elif valor < 50.0:
    print('Lucro de 40%:', valor*1.4)
else: 
    print('Lucro de 30%:', valor*1.3)
=====================================================================================
#4- Elabore um programa em Python que implemente uma calculadora com as funções de somar, subtrair, multiplicar e dividir. 
#O programa deverá solicitar ao usuário os dois valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e mostrar o resultado.

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
operacao = input('Digite o sinal da operação que deseja: ')
if operacao == '+':
    print(f'Você selecionou soma e o resultado de {n1} + {n2} é:', (n1+n2))
elif operacao == '-':
    print(f'Você selecionou subtração e o resultado de {n1} - {n2} é:', (n1-n2))
elif operacao == '*':
    print(f'Você selecionou multiplicação e o resultado de {n1} * {n2} é:', (n1*n2))
elif operacao == '/':
    print(f'Você selecionou soma e o resultado de {n1} / {n2} é:', (n1/n2))
else: 
    print('ERRO! Digite um operador valido! (Ex: +, -, *, /)')
