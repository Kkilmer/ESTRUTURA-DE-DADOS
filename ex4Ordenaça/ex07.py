#7. Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
from random import randint
def decrescente(lista_vetor):
    for i in range(len(lista_vetor)):
        menor_index = i
        for j in range(i+1, len(lista_vetor)):
            if lista_vetor[j] > lista_vetor[menor_index]:
                menor_index = j
        lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]
n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = []
for  i in range(0, n):
    lista_vetor. append(randint(1, 20))
print(f"Lista original: {lista_vetor}")
decrescente(lista_vetor)
terceiro_maior = lista_vetor[2]
print(f"O terceiro maior valor é: {terceiro_maior}")

