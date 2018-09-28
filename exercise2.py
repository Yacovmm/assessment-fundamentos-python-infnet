import sys

n1 = int(input("Insira o n1:"))
n2 = int(input("Insira o n2:"))
cont = 0

if n2 == 0:  sys.exit("N2 igual a 0")


def isEqual(n1, n2):
  return n1 >= 0 and n2 >= 0 or n1 <= 0 and n2 <= 0


while(isEqual(n1, n2)):
  n1 -= n2
  cont += 1
  print("while positivo", cont)

while(not isEqual(n1, n2)):
  n1 += n2
  cont -= 1
  print("while negativo", cont)


print(cont)

"""
o programa basicamente verifica se os dois números possuem 
simbolos iguais e subtrai um elemento pelo segundo caso tenham simbolos iguais, 
e soma caso não sejam iguais, no final imprime um contador com a quantidade de itereções que teve até que a condção se desfez.
"""