#1
a = [1, 0, 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
a[4] = 100
print(a[0],"\n",a[1],"\n",a[2],"\n",a[3],"\n",a[4])

#2
numeros = input("Digite seis numeros inteiros, e separe por espaço").split()
print(numeros)

#3
vetor = [0] * 10
quadrado = [0] * 10

for i in range(10):
    vetor[i] = int(input("Digite um numero inteiro "))

for i in range(10):
    quadrado[i] = vetor[i]**2
print(vetor)
print(quadrado)

#4
vetor2 = [0] * 8
for i in range(8):
    vetor2[i] = int(input("Digite um valor "))
valorx = int(input("Digite um novo numero inteiro"))
valory = int(input("Digite um novo numero inteiro"))
vetor2[2] = valorx
vetor2[3] = valory

soma = vetor2[2] + vetor2[3]
print(soma)

#5
vetor3 = [0] * 10
for i in range(10):
    vetor3[i] = int(input("Digite um valor"))
cont = 0
pares = 0
while cont < 10:
    if vetor3[cont] % 2 == 0:
        pares += 1
    cont += 1
print(f"Quantidade de números pares: {pares}, seus números: {vetor3}")

#6
vetor4 = [0] * 10
for i in range(10):
    vetor4[i] = int(input('Digite um valor: '))
    if vetor4[i] > vetor4[0]:
        vetor4[0] = vetor4[i]
    elif vetor4[i] < vetor4[1]:
        vetor4[1] = vetor4[i]
print(vetor4)
print(f"Seu maior número é {vetor4[0]}, e seu menor número é {vetor4[1]}")

#7
vetor5 = [0] * 10
indice = 0
for i in range (10):
    vetor5[i] = int(input('Digite um valor: '))
for i in range(1, 10):
    if vetor5[i] > vetor5[indice]:
        indice = i
print(vetor5)
print(f"Seu maior número está na posição {indice}")

#8
notas = [0] * 15
soma = 0
for i in range(15):
    notas[i] = float(input('Digite a nota do aluno: '))
    soma = soma + notas[i]
    media = soma / 15
print(media)

#9
vetor6 = [0] * 10
negativos = 0
soma = 0
for i in range(10):
    vetor6[i] = int(input('Digite um valor: '))
    if vetor6[i] < 0:
        negativos += 1
        soma = soma + vetor6[i]
print(vetor6)
print(negativos)
print(soma)

#10
vetor7 = [0] * 5
soma = 0
for i in range(5):
    vetor7[i] = int(input("Digite um valor"))
    if vetor7[i] > vetor7[0]:
        maior = vetor7[i]
    elif vetor7[i] < vetor7[1]:
        menor = vetor7[i]
    soma = soma + vetor7[i]
    media = soma / 5
print(vetor7)
print(f"Seu maior número é {maior}, e seu menor número é {menor}")
print(f"Essa é a média dos seu números {media}")

#11
vetor8 = [0] * 5
indice_maior = 0
indice_menor = 0
for i in range(5):
    vetor8[i] = int(input('Digite um valor: '))
for i in range(1, 5):
    if vetor8[i] > vetor8[indice_maior]:
        indice_maior= i
    elif vetor8[i] < vetor8[indice_menor]:
        indice_menor = i
print(vetor8)
print(f"Seu maior número está na posição {indice_maior} e seu menor número está na posição {indice_menor} ")
