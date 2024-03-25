#5. Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos 
# duplicados, retornando o vetor resultante sem duplicatas.

from random import randint
n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = []
for  i in range(0, n):
    lista_vetor. append(randint(1, 5))
print(f"Lista original: {lista_vetor}")
#def removeDuplicatas(v):
#    return list(set(v))
def removeDuplicatas(vetor):
    sem_repetir = []
    for i in vetor:
        if not sem_repetir or i != sem_repetir[-1]:
            sem_repetir(i)
    return sem_repetir
print(f"Lista sem valores repetidos: {removeDuplicatas(lista_vetor)}")
