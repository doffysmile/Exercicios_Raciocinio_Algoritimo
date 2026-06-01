from itertools import count
while True :
    palavra = input("Informe uma palavra de no mínimo 3 letras e no máximo 10:")
    conta = len(palavra)
    if 3 >= conta or conta >= 10:
        print("Digite uma palavra dentro das regras")
    else:
        print(f"Sua palavra {conta} letras")
    break

#1
nota = float(input("Informe uma nota:"))
while 0 >= nota or nota > 10:
    print("Sua nota é inválida, tente novamente")
    nota = float(input("Informe uma nota:"))
print("Sua nota é válida")

#2
num = int(input("Informe um número:"))
soma = 0
i = 1
while i <= num:
    soma += i
    i += 1
print(soma)

#3
num = float(input("Informe um número: "))
soma = 0
quant = 0
nums = 0
while num != -1:
    if num != -1:
        soma += nums
        quant += 1
    else:
        media = soma/quant
        print(media)

#4
pares = 0
impares = 0
count = 1

while count <= 10:
    num = int(input("Informe um número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    count+= 1

print(pares)
print(impares)




