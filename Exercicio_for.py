# 1
for i in range (1, 101):
    if i % 3 == 0:
        print(f"Multiplo de 3 {i}")
    elif i % 5 == 0:
        print(f"Multiplo de 5 {i}")

# 2
num = int(input("Informe um numero inteiro:"))
while num <= 0:
    num = int(input("Informe um numero inteiro!:"))

soma = 0
expre = ""

for i in range(1,num + 1):
    soma += i
    if i < num:
        expre += f"{i} +"
    else:
        expre += f"{i}"
print(f"{expre} = {soma}")

# 3
num1 = int(input("Informe um numero inicial para seu intervalo:"))
num2 = int(input("Informe um número final para seu intervalo:"))

for num in range (num1, num2 +1):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
#4
linha = int(input("Informe a quantidade de linhas:"))

for i in range(1, linha +1):
    for j in range(1, i +1):
        print(j, end=" ")
    print()


