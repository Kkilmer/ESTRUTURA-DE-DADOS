#3. Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da lista.
from random import randint
numeros = []
soma = 0
qnt = int(input("A lista deve conter quantos números? "))
for i in range(qnt):
    num = randint(0, 50)
    numeros.append(num)
for n in numeros:
    soma += n
    
print(f"Sua lista é {numeros} e a soma dos valores é {soma}.")