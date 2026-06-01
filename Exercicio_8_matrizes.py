#1
matriz = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

for matriz[0][0] in range(5):
    matriz[0][0] = 1
    for matriz[1][1] in range(4):
        matriz[1][1] = 1
        for matriz[2][2] in range(3):
            matriz[2][2] = 1
            for matriz[3][3] in range(2):
                matriz[3][3] = 1
                for matriz[4][4] in range(1):
                    matriz[4][4] = 1
                    for matriz[5][5] in range(0):
                        matriz[5][5] = 1
for linha in range(5):
        print(matriz[linha])

#2
matriz2 = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
maior = 0
for i in range(4):
    for j in range(4):
        matriz2[i][j] = int(input("Digite um número inteiro:"))
        if matriz2[i][j] > maior:
            maior = matriz2[i][j]
print(matriz2)
print(maior)

#3
matriz3 = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
alunos = 0
alunoMaiorMadia = matriz3[0][0]
mediaMaior = matriz3[0][3]

while alunos < 3:
    #matricula
    for j in range(5):
        matriz3[j][0] = float(input("Digite seu número de matricula"))
    for i in range(5):
        print(matriz3[i])
    #provas
    for j in range(5):
        matriz3[j][1] = float(input("Digite suas notas de provas"))
    for i in range(5):
        print(matriz3[i])
    #trabalhos
    for j in range(5):
        matriz3[j][2] = float(input("Digite suas notas de trabalhos"))
    #nota final
    for j in range(5):
        matriz3[j][3] =  (matriz3[j][1] + matriz3[j][2])/ 2
        if matriz3[j][3] > mediaMaior:
            mediaMaior = matriz3[j][3]
            alunoMaiorMadia = matriz3[j][0]
    for i in range(5):
        print(matriz3[i])
    alunos += 1

for i in range(5):
    print(matriz3[i])
    print(f"Aluno com a maior média: {alunoMaiorMadia}, sua média foi: {mediaMaior}")




