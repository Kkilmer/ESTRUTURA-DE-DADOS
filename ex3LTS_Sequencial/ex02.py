#2. Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista.
lista_nomes= []
continua = "s"
qnt = 0
while continua == "s": 
    nome = str(input("Digite um nome:").capitalize())
    if nome == "":
        print("Você não digitou nenhum nome.")
    else:
        lista_nomes.append(str(nome))
        qnt += 1
    continua = str(input("Gostaria de continuar? (S/N): ").lower())
if qnt == 0:
    print("Você não digitou nenhum nome.")
else:
    print(f"Foram  digitados {qnt} nomes:{lista_nomes}")