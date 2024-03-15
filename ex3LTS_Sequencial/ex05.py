#5. Escreva um programa que cria uma lista de palavras e exibe a quantidade de 
# palavras que começam com a letra 'A'.
lista_palavra = []
continua = "s"
palavra_com_a = 0
while continua == "s": 
    nome = str(input("Digite uma palavra:").capitalize())
    if nome == "":
        print("Você não digitou nenhuma palavra.")
    else:
        lista_palavra.append(str(nome))
    continua = str(input("Gostaria de continuar? (S/N): ").lower())
    
for i in lista_palavra:
    if i[0] == "A":
        palavra_com_a += 1
if palavra_com_a == 0:
    print("Não há palavra que comece com a letra A")
elif palavra_com_a == 1:
    print(f"A lista tem uma palavra que inicia com a letra A")
else:
    print(f"A lista tem {palavra_com_a} palavras que iniciam com a letra A")
