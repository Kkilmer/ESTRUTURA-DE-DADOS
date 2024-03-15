#4. Escreva um programa que cria uma lista de números inteiros e exibe a média dos números da lista.
from random import randint
numeros = []
soma = 0
contador = 0
qnt = int(input("A lista deve conter quantos números? "))
for i in range(qnt):
    num = randint(0, 50)
    numeros.append(num)
for n in numeros:
    soma += n
    contador += 1
media = soma / contador
print(f"Os números gerados foram {numeros}.")
print(f"A média dos valores é {media:.2f}.")