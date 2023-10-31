#1 - Escreva um programa em Python que resolva o problema: “Um Programador com insônia”, representado ao lado. Utilize o comando de repetição apropriado para o problema.

#Obs: Exibir no final o número de carneirinhos contados.

#carneirinhos = 0
#while True:
#    resposta = input("Você ja dormiu? (sim/não): ")
#    
#    if resposta == "sim":
#        break
#    else:
#        carneirinhos += 1
        
#print (f"Eu contei {carneirinhos} carneirinhos antes de dormir") #

#=================================================================================

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
        idade = int(input("Digite sua idade: "))
        if idade < 16:
            print('Você não pode votar')
            somaIdade += idade
            naoEleitor += 1
        elif idade < 18 or idade > 65:
            print("Facultativo: Vota se quiser")
            eleitor += 1
        else:
            print('Obrigatório vá votar imediatamente')
            eleitor += 1
    else:
        break

print(f"\nA quantidade de alunos que podem votar é de {eleitor}")
print(f"\nA média dos alunos que não são eleitores é de {somaIdade/naoEleitor}")          


    