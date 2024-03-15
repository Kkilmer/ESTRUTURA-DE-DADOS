#1. Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista.
from random import randint
lista = []
qnt = int(input("A lista deve conter quantos números? "))
def valormax(lista):
    maior = 0
    if len(lista) > 0:
        for valor in lista:
            if valor > maior:
                maior = valor
        return maior
    else:
        print("A lista está vazia.")
for i in range(qnt):
    num = randint(1, 20)
    lista.append(num)
print("A lista gerada foi: ", (lista))   
print("O valor máximo nesta lista é: ",valormax(lista))
