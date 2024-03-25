#4. Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número. 
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
from random import randint
n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = []
for  i in range(0, n):
    lista_vetor.append(randint(1, 20))
print(f"Lista original: {lista_vetor}")  
for i in range(len(lista_vetor)):
    menor_index = i
    for j in range( i+1, len(lista_vetor)):
        if lista_vetor[j]<lista_vetor[i]:
            menor_index = j
            lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]
print(f"{lista_vetor[1]} é o segundo menor valor.")