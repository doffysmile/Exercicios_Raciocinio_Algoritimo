import random
#1
num = [0]* 10

for i in range (10):
    num[i] = i + 1
print(num)

#2
num2 = [0] * 3
for i in range (3):
    num2[i] = int(input('Digite um numero inteiro:'))
print(num2)

#3
frase = [""] * 1
for i in range (1):
    frase[i] = input('Digite uma frase: ')
print(frase)

#4
num3 = [0] * 10
for i in range (0,10):
    num3[i] = int(input('Digite um numero inteiro: '))
    if num3[i] > num3[i]:
        num3[0] = num3[i]
print(num3)

#5
palavras = [""] * 5
maior = palavras[0]
menor = palavras[0]
for i in range(5):
    palavras[i] = input('Digite uma palavra: ')
    if len(palavras[i]) > len(maior):
        maior = palavras[i]
    if len(palavras[i]) < len(menor):
        menor = palavras[i]

print("Maior: ", maior)
print("Menor: ", menor)

6
impar = [1, 3, 5, 7, 9]
par = [2, 4, 6, 8, 10]
juncao = [0] * 10

i = 0
j = 0
k = 0

while i < 5 and j < 5:
    if impar[i] < par[j]:
        juncao[k] = impar[i]
        i += 1
    else:
        juncao[k] = par[j]
        j += 1
    k += 1
while i < 5:
    juncao[k] = impar[i]
    i += 1
    k += 1
while j < 5:
    juncao[k] = par[j]
    j += 1
    k += 1
print(juncao)

7
num4 = [0] * 100
for i in range(100):
    num4[i] = i + 1
for i in range(100):
    if num4[i] % 2 == 0:
        print(num4[i])

8
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_sqr = [0] * 10
soma = 0
for i in numeros:
    num_sqr[i] = numeros[i] ** 2
    soma = soma + numeros[i]
print(soma)
print(num_sqr)

#9
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random.shuffle(alfabeto)
letra = random.choice(alfabeto)
posição = int(input(f"Digite a posição de {letra} do alfabeto"))

if alfabeto[posição] == letra:
    print("Você acertou")
else:
    print("Você verrou")

#10
