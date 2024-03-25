#6. Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida,
# conte quantos números pares e quantos números ímpares existem no vetor ordenado.
from random import sample
def decrescente(lista_vetor):
    for i in range(len(lista_vetor)):
        menor_index = i
        for j in range(i+1, len(lista_vetor)):
            if lista_vetor[j] > lista_vetor[menor_index]:
                menor_index = j
        lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]
par = 0
impar = 0
n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = sample(range(0, 99), n)
for i in range(len(lista_vetor)):
        if  lista_vetor[i] % 2 == 0:
            par +=1
        else:
            impar +=1
print(f"Lista original: {lista_vetor}")
decrescente(lista_vetor)
print(f"Lista decrescente: {(lista_vetor)}")
print(f"A lista contém {par} números pares e {impar} números ímpares.")
