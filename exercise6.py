"""
Escreva um programa em Python que leia um vetor de 5 números inteiros
e o apresente na ordem inversa de leitura. Imprima o vetor, no final. Use listas.
"""

lista = []

for i in range(1, 6):
    a = int(input("Insira um número:"))
    lista.append(a)

print(lista[::-1])
print(lista)
