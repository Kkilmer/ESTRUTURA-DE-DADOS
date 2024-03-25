#1. Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.
from random import sample
n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = (sample(range(0, 99), n))
print(f"Lista original: {lista_vetor}")  
for i in range(len(lista_vetor)):
    menor_index = i
    for j in range( i+1, len(lista_vetor)):
        if lista_vetor[j]<lista_vetor[i]:
            menor_index = j
            lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]
print(f"Lista organizada: {lista_vetor}")
