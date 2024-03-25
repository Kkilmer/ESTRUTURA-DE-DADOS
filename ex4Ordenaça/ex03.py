#3. Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem 
# usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.
from random import sample

def crescente(lista_vetor):
    for i in range(len(lista_vetor)):
        menor_index = i
        for j in range(i+1, len(lista_vetor)):
            if lista_vetor[j] < lista_vetor[menor_index]:
                menor_index = j
        lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]

def decrescente(lista_vetor):
    for i in range(len(lista_vetor)):
        menor_index = i
        for j in range(i+1, len(lista_vetor)):
            if lista_vetor[j] > lista_vetor[menor_index]:
                menor_index = j
        lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]

n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = sample(range(0, 99), n)
print(f"Lista original: {lista_vetor}")

resposta = input("Você gostaria de Menor ou Maior valor da lista? (MENOR/MAIOR) ").strip().upper()

try:    
    if resposta == "MENOR":
        crescente(lista_vetor)
        print(f"Lista em ordem crescente: {lista_vetor[0]}")
    elif resposta == "MAIOR":
        decrescente(lista_vetor)
        print(f"Lista em ordem decrescente: {lista_vetor[0]}")
    else:
        print("Você digitou uma opção inválida.")
except ValueError:
    print("Você digitou um valor inesperado.")
