#2. Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
# serve como chave para realizar a ordenação crescente ou decrescente.
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

resposta = input("Você gostaria de ver a lista em ordem crescente ou decrescente? (C/D) ").strip().upper()

try:    
    if resposta == "C":
        crescente(lista_vetor)
        print(f"Lista em ordem crescente: {lista_vetor}")
    elif resposta == "D":
        decrescente(lista_vetor)
        print(f"Lista em ordem decrescente: {lista_vetor}")
    else:
        print("Você digitou uma opção inválida.")
except ValueError:
    print("Você digitou um valor inesperado.")
