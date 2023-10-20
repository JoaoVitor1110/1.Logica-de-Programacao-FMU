#Ex.1 Tabuada
num = int(input("Digite um numero inteiro: "))
for i in range(11):
    print("%d * %d = %d" %(num, i, num*i))

#Ex.2 - Soma Total
#Uma ocasião é começar a variavel range(11) e o pode ficar sem a soma = 0
soma = 0
for i in range(6):
    num = float(input("Digite um numero real: "))
    soma = soma + num
    
print("O resultado da soma é: ",soma)

#Ex.3 - Média de 10 alunos

contador = 0
while contador <= 10:
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2)/2
    print("A média é %.2f" %media) #%.2f serve pra concatenar dois numeros após a virgula
    contador = contador + 1 

#Ex.4 - Carrinho de Compras

contador = 0 
soma = 0
resp = "s"

while resp == 's' or resp == 'S':
    num = float(input("Qual o valor do item: "))
    soma = soma + num
    contador = contador + 1 
    resp = input("Deseja continuar (S/N)? ")
    
media = soma / contador    
print("o total do seu carrinho somou: %.2f" %soma)
print("A média dos itens é de: %.2f" %media)
