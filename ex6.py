# ESCREVA UM PROGRAMA QUE PEÇA UM NUMERO INTEIRO POSITIVO AO USUARIO 
# E CALCULE O FATORIAL DESSE NUMERO.

numero = int(input('Fatorial de: '))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)