""""
Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter dois argumentos inteiros
A e B e calcular A elevado B usando multiplicações sucessivas (não use a função de python math.pow) e
retornar o resultado da operação. Depois, crie um programa em Python
que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.
"""

base = int(input("Entre com o valor da base: "))
exp  = int(input("Entre com o valor do expoente: "))
cont = exp
resultado = 1
while cont > 0:
  resultado = resultado * base
  cont = cont - 1

print(resultado)