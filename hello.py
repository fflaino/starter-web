#-*- coding: utf-8 -*-
"""
var1 = 1 # variavel inteira
var2 = 1.1 # variavel float
var3 = "Eu sou uma string" # variavel string
var4 = True # verdadeiro
var4 = False # falso

print(var1)
print(var2)
print(var3)
print(var4)

__________________________________

x = 1
y = 1000000000

if x > y:
	print("x é maior que y")

if y > x:
	print("y é maior que x")


__________________________________

x = 1
y = 2

if x > y:
	print("x maior que y")
else:
	print("x não é maior que y")

___________________________________

x = 1
y = 2

if x == y:
	print("Números iguais")
elif x < y:
	print("x menor que y")
elif y > x:
	print("y maior que x")
else:
	print("Números diferentes")


___________________________________

x = 1

while x < 10:
	print(x)
	x += 1 # x = x + 1

__________________________________

lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoto",9.99,True]

for i in lista3:
	print(i)

__________________________________

for i in range(10,20,2):
	print(i)

__________________________________

a = "Felipe"
b = "Laino"

concatenar = a + " " + b

tamanho = len(concatenar)

print(concatenar[0:4])

_______________________________

a = "Felipe"
b = "Laino"

concatenar = a + " " + b

print(concatenar)
print(concatenar.lower())
print(concatenar.upper())

______________________________________

a = "Felipe"
b = "Laino"

concatenar = a + " " + b

print(concatenar)
concatenar = concatenar.upper()

print(concatenar)

_____________________________________

a = "Felipe"
b = "Laino"

concatenar = a + " " + b + " "

print(concatenar.strip())

______________________________________

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split("r")
print(minha_lista)

_________________________________________

minha_string = "O rato roeu a roupa do rei de Roma"

busca = minha_string.find("rainha")
print(busca)

print(minha_string[busca:])

______________________________________________

minha_string = "O rato roeu a roupa do rei de Roma"

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

_______________________________________________

def soma(x,y):
	return x+y

def multiplicacao(x, y):
	return x*y

s = soma(2, 3)
m = multiplicacao(3, 4)

print(soma(s, m))

___________________________________________________

arquivo = open("C:/Projetos-BI/Python/arquivo.txt")

texto_completo = arquivo.read()
print(texto_completo)

"""

w = open("arquivo.txt", "a")

w.write("Esse é o meu arquivo\n")

w.close()