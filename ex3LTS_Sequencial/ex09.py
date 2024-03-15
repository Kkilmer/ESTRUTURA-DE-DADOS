#9. Escreva um programa que cria duas listas de números inteiros 
# e exibe os números que estão presentes em ambas as listas.
from random import randint
lista1 = []
lista2 = []
comum = []
n = int(input("Quantos números deverão se gerados nas listas?"))
for  i in range(n):
    num = randint(1, 20)
    lista1.append(num)
    num = randint(1, 20)
    lista2.append(num)
for  num in lista1:
    if num in lista2:
        comum.append(num)
print (f"Vezes que os números se repetem: {len(comum)} \nSão eles: {comum}")