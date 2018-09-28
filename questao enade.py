vetA = [0] * 10  # cria vetor de 10 posições
vetB = [0] * 10  # cria vetor de 10 posições
for i in range(0, 10):
    vetB[i] = 0
    if i % 2 == 0:
        vetA[i] = i
    else:
        vetA[i] = i * 2

for i in range(0, 10):
    while vetA[i] > i:
        vetB[i] = vetA[i]
        vetA[i] = vetA[i] - 1


        '''
        Resposta:

            vetA: [0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
            vetB: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            vetA: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
            vetB: [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
'''