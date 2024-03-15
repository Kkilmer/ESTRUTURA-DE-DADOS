#10. Escreva um programa que cria uma lista de números inteiros e remove todos os números repetidos,
# exibindo a lista resultante.
from random import sample #sample gera numeros aleatorios sem repetir
comum = []
n = int(input("Quantos números serão gerados em cada lista?"))
lista1 = sample(range(99), n) 
lista2 = sample(range(99), n)
for num in lista1:
    if num not in lista2:
        comum.append(num)
for num in lista2:
    if num not in lista1:
        comum.append(num)
print(lista1)
print(lista2)
print (f"Os números que não se repetem são: {sorted(comum)}") 