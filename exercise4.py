"""'
Usando o Thonny, escreva um programa em Python que some todos os 
números pares de 1 até um dado N, inclusive. N deve ser obtido do usuário. No final, escreva 
o valor do resultado desta soma.
"""


def SomarNums(n):
    pares = [num for num in range(n) if (num % 2 == 0)]
    print(pares)


SomarNums(int(input("Entre com um número:")))
