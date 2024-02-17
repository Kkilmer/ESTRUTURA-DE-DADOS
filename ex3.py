# ESCREVA UM PROGRAMA QUE SOLICITE UM NUMERO AO USUARIO
# E IMPRIMA TODOS OS NUMEROS PARES DE 0 ATÉ ESSE NUMERO.

valor = int(input('insira um valor: '))

for valor in range(5):
    if valor % 2 == 0:
        print('é pares de 0')
    else:
        print('não é')
