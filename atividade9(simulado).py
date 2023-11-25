"""Questão 1
#Escreva um programa em Python que imprima os números de 1 a 10.
for c in range (1,11):
    print(c, end=" ")
#Questão 2
#Escreva um programa em Python que solicite ao usuário um número e imprima o seu quadrado.
num = float(input("Insirá um numero: "))
num = num**2
print(f"Seu numero ao quadrado fica {num}")
#Questão 3
#Escreva um programa em Python que solicite ao usuário dois números e imprima a soma, a diferença, o produto e a divisão deles.
n1 = int(input("Insirá um número: "))
n2 = int(input("Insirá outro número: "))
print(f"A soma resultará em {n1+n2} ")
print(f"A diferença resultará em {n1-n2} ")
print(f"O produto resultará em {n1*n2} ")
print(f"A divisão resultará em {n1/n2} ")

#Questão 4
#Escreva um programa em Python que solicite ao usuário uma lista de números e imprima a soma deles.
soma = 0
print("Digite digite 9999 que o programa efetuará a soma")
while True:
    numeros = int(input("Escreva um numero: "))
    if (numeros == 9999):
        break
    soma += numeros    
print(soma)

#Questão 5
#Escreva um programa que imprima os números de 1 a 100, um por linha.
for c in range(1,101):
    print(c)

#Questão 6
#Escreva um programa que solicite um número ao usuário e imprima se o número é par ou ímpar.
num = int(input("Escreva um numero: "))
if (num % 2 == 0):
    print("Numero Par")
else:
    print("Numero Impar")

#Questão 7
#Escreva um programa que solicite três números ao usuário e imprima o maior deles.
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

#Questão 8
#Escreva um programa que crie uma lista com os nomes dos meses do ano. Em seguida, imprima a lista.
meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print("Meses do ano:")
for mes in meses_do_ano:
    print(mes)

Questão 9
Qual é o resultado da expressão 5 * 2 + 3?
● 13

Questão 10
Qual é o tipo da variável a no trecho de código abaixo?
Python
a = "Olá, mundo!"
● str

Questão 11
Qual é o resultado da expressão "Olá, mundo!".upper()?
● "OLÁ, MUNDO!"

Questão 12
Qual é a saída do seguinte código?
Python
for i in range(1, 11):
print(i)
● 1 a 10

Questão 13
Qual é a função do operador + em Python?
● Adiciona dois números

Questão 14
● Qual é a diferença entre if e elif?
if é uma condição
já um elif é um outro caminho com outra condição
para seter um elif precisa se ter um if
e elif é a abreviação de else if que ja é uma abreviação de else {
    if{

    }
}
Questão 15
● Como você cria uma lista em Python? 
Podemos criar uma lista adicionando os dados entre colchetes e com a função for
"""