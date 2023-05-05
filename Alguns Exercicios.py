# contao números de 'a' da palavra banana
palavra = 'banana'
contador = 0
for letra in palavra:
    if letra == 'a':
        contador = contador + 1
print(contador)

print()
print()
# Calculo da área de um triangulo

def area_triangulo():
  base=int(input("Introduza o valor da base: "))
  altura=int(input("Introduza o valor da altura: "))
  area_triangulo=(base*altura)/2
  print("A área do triângulo é: ", area_triangulo)
area_triangulo()

print()
print()
# Cálculo do IMC

def IMC():
    peso = eval(input("Digite o seu peso:"))
    altura=eval(input("Digite a sua altura:"))
    Imc= (peso/altura**2)
    print("O seu indíce de massa corporal é:")
    print(Imc)
    if (Imc) > 25:
        print("Precisa de perder peso")
    else: 
        print("Está em boa forma física")
IMC()   


print()
print()
#Calculo de uma percentágem do desconto de uma compra

preço = float(input( "Indique o valor da compra:")) 
desconto = float(input( "Indique percentagem do desconto:"))
valor_do_desconto = preço * desconto / 100 
a_pagar = preço - valor_do_desconto 
print( "Um desconto de %1.2f %% numa mercadoria de € %1.2f." %(desconto, preço)) 
print( "O valor do desconto é de €.", valor_do_desconto)
print( "O valor a pagar é de € %1.2f." % (a_pagar))


print()
print()
# Calcular um valor em metros e reduz para milímetros

metros = float(input( "Indique o valor em metros: ")) 
milímetros = metros * 1000 
print("%10.2f metros representam %10.2f em milímetros." % (metros, milímetros))

print()
print()
#Conta o número de dígitos de um número

print("Vamos contar dígitos de um número.")
digitos = int(input("Indique um número para contar os seus dígitos : "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador+= 1
print("Total de dígitos é: ", contador)

print()
print()
#Tabuada

numero = int(input('Informe o numero para calcular a tabuada: '))

print('\n Tabuada de', numero, ':')

for i in range(1, 11):
    print(numero, 'X', i, '=', (numero * i))

# Garantir que caso o utilizador colocasse uma letra em vez de um numero aparece-se uma mensagem avisar

num = input("Insira um número à sua escolha, positivo, negativo ou zero:\n" )

txt = num.isnumeric()
if (txt):
  num = int(num)
  if num == 0: 
    print("O numero inserido", num, "é igual a zero.")
  elif num > 0:
    print("O numero inserido", num, "é positivo.")
  elif num < 0:
    print("O numero inserio", num, "é negativo.")
else:
  print("Insira um número, sff")

print()
print()
#33 Exercicio para calcular se um numero é par

num = eval(input("Digite um número: "))
if(num % 2 == 0):
    print("Número é par.")
else:
    print("Número é ímpar")

#34 Verificar se um numero é redondo

  
print()
print()   
#36 Pedir 2 valores  fazer a divisão e o resto e exibe o resultado da divisão e do resto
    
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2
print()
print(num1, "divido por", num2, "é igual a: ", divisao)
print("O resto da divisão entre", num1, "e", num2, " é igual a:", resto)   

print()
print()
#42.	Faça um programa que receba a idade de um utilizador e exiba se a idade introduzida se é de uma 
#criança, adulto ou idoso(criança – 12 anos, adolescente – 18, adulto –67 e idoso)."""

idade = eval(input("Indique uma idade: "))
if idade < 12:
    print('criança')
elif idade < 18:
    print('adolescente')
elif idade < 67:
    print('adulto')
else:
    print('idoso') 

print()
print()

# Introduza as cordenadas para lhe devolver o ângulo e o raio
def coordenadas():
    import math
    x,y=eval(input("Introduza o valor de x e de y: "))
    r=math.sqrt(x**2+y**2)
    angulo=math.atan(y/x)
    print("r=",r, "angulo=",angulo)

coordenadas()

print()
print()
#A Unidade Astronómica (UA)

def periodo():
    import math
    a=eval(input("Introduza a distância em UA: "))
    p=math.sqrt(a**3)
    print("Período: ",p)

periodo()


print()
print()
#Calcular o cambio do euro para o dolar

def cambio():
    euros=eval(input("Introduza o valor em euros: "))
    dolares=euros/0.98
    print("O valor em dólares é: ",dolares)
cambio()