#8 - Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor domeio quando o vetor é ordenado.
# Certifique-se de que sua função funcione para vetores com um número ímpar de elementos.
from random import sample
def crescente(lista_vetor):
    for i in range(len(lista_vetor)):
        menor_index = i
        for j in range(i+1, len(lista_vetor)):
            if lista_vetor[j] < lista_vetor[menor_index]:
                menor_index = j
        lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]
        
n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = sample(range(0, 99), n)
print(f"Lista original: {lista_vetor}")
crescente(lista_vetor)
if len(lista_vetor) % 2 == 0:
    index_maior = int((len(lista_vetor)/2)+1)
    index_menor = int((len(lista_vetor)/2)-1)
    tamanho = int((lista_vetor[index_menor]+lista_vetor[index_maior])/2)
    print(tamanho)
    print(f"A mediana da lista é {(lista_vetor[tamanho])}")
else:
    tamanho =  int(len(lista_vetor)/2)
    print(tamanho)                                          
    print(f"A mediana da lista é {(lista_vetor[tamanho])}")
    