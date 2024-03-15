#7. Escreva um programa que cria uma lista de números inteiros e exibe os números pares da lista.
numeros = [4, 6, 8, 3, 12, 1, 5, 9, 7]
par = []
while True:
    reposta = input("Você quer adicionar uma número a lista? (S/N) ").upper()[0]
    if reposta == "S":
        numero = int(input("Digite um número inteiro: "))
        if not int:
            print("Isso não é um número! Tente novamente.")
        else:
            numeros.append(int(numero))
    elif reposta == "N":
        break
    else:
        print("Opção inválida! Tente novamente.")
for i in numeros:
    if i % 2 == 0:
        par.append(i)
print("Números Pares: ", par)