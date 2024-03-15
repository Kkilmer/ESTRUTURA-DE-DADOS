#6. Escreva um programa que cria uma lista de strings e exibe a mais longa palavra da lista.
lista = []
maior_palavra = ""
while True:
    reposta = input("Você quer adicionar uma palavra a lista? (S/N) ").upper()[0]
    if reposta == "S":
        palavra = str(input("Digite a palavra: "))
        lista.append(palavra)
    elif reposta == "N":
        break
    else:
        print("Opção inválida! Tente novamente.")
for palavra in lista:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
print(f'A palavra mais longa é "{maior_palavra}" com {len(maior_palavra)} letras')
