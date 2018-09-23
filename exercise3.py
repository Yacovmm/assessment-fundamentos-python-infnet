'''
3
Usando o Thonny, escreva um programa em Python que leia três números inteiros
, n1, n2 e n3, e os imprima em ordem crescente.
'''

n1 = int(input("Entre com o primeiro número:"))
n2 = int(input("Entre com o segundo número:"))
n3 = int(input("Entre com o terceiro número:"))
lista = [n1,n2,n3]

print(sorted(lista, key=int))
