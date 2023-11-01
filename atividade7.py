#1 - Escreva um programa em Python que resolva o problema: “Um Programador com insônia”, representado ao lado. Utilize o comando de repetição apropriado para o problema.

#Obs: Exibir no final o número de carneirinhos contados.

carneirinhos = 0
while True:
    resposta = input("Você ja dormiu? (sim/não): ")
    
    if resposta == "sim":
        break
    else:
        carneirinhos += 1
        
print (f"Eu contei {carneirinhos} carneirinhos antes de dormir") 


#2- Faça um programa em Python que recebe a idade de cada um dos 500 alunos de uma escola, matriculados no Ensino Médio. O algoritmo deverá verificar, calcular e imprimir:
#a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16 anos.
#b) a média da idade dos alunos que não são eleitores.

somaIdade = 0
eleitor = 0
naoEleitor = 0
#Calcular Idade
while True: 
    cadastro = input("Deseja cadastrar a idade de um aluno? (S/N): ")

    if cadastro.upper() == 'S':
        idade = int(input("Digite a idade: "))
        if idade < 16:
            print('Não pode votar')
            somaIdade += idade
            naoEleitor += 1
        elif idade < 18 or idade > 65:
            print("Facultativo: Vota se quiser")
            eleitor += 1
        else:
            print('Obrigatório votar')
            eleitor += 1
    else:
        break

print(f"\nA quantidade de alunos que podem votar é de {eleitor}")
print(f"\nA média dos alunos que não são eleitores é de {somaIdade/naoEleitor}")      

#3-  Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um programa em Python que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário.    

salario = float(input("Qual o valor do seu salario: R$"))
vendas = float(input("Quanto você vendeu: R$"))
comissao = vendas * 0.04
input(f"Seu é de R${salario}, vendeu R${vendas} e você recebeu de comissão R${comissao}, logo fechou o mês com {salario+comissao}")
 
#4- Faça um programa em Python que solicite ao usuário uma quantidade de segundos, calcule e exiba a quantidade de horas, minutos e segundos.

segundos = float(input("Digite uma quantidade de segundos: "))
horas = segundos/3600
minutos = segundos / 60
input(f"A  quantidade que você digitou, em horas ficará: %.2f horas, e em minutos ficara: %.2f" %(horas, minutos))

#5- Faça um programa em Python que solicite ao usuário sua altura e sexo, calcule e imprima o seu peso ideal. Utilize a seguinte convenção:

#§Para homens: (72.7*h) – 58
#§Para mulheres: (62.1*h) – 44.7

altura = float(input("Qual sera altura cadastrada? (em metros) = "))
sexo = input("Qual é o sexo da pessoa? (M/H) = ")
if sexo.upper() == "M":
    pesoIdealMulher = (62.1*altura)-44.7
    print("O peso ideal de uma mulher desta altura deve ser de %.2fkgs" %(pesoIdealMulher))
else:
    pesoIdealHomem = (72.7*altura)-58
    print(f"O peso ideal de um homem desta altura deve ser de %.2fkgs" %(pesoIdealHomem))

#6- Faça um programa em Python para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Obs: A quantidade de latas deverá ser um número inteiro. Utilize a biblioteca math:

m2 = float(input("Quantos metros quadrados será pintado? "))
tintaUsada = m2 / 54
preco = 80
if m2 < 54:
    tintaUsada = 1

print("Você precisará de", int(tintaUsada), "galões e custará R$%.2f" %(preco*tintaUsada))

#7- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela:

#O programa deverá mostrar na tela o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E


n1 = float(input("Qual a primeira nota do aluno? => "))
n2 = float(input("Qual a segunda nota do aluno? => "))
media = (n1+n2)/2
print(f"A média do aluno foi {media}")
if media >= 9:
    print("Conceito A - Aprovado")
elif media >= 7.5 and media < 9:      
    print("Conceito B - Aprovado")
elif media >= 6 and media < 7.5:      
    print("Conceito C - Aprovado")
elif media >= 4 and media < 6:      
    print("Conceito D - Reprovado")
else:        
    print("Conceito E - Reprovado")