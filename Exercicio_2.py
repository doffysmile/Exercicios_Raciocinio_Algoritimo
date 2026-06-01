#Idade atravez do ano de nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")

#Locadora
dias = int(input("Quantos dias você deseja locar o carro? "))
valor_diaria = 100.00
total = dias * valor_diaria
print(f"Total a pagar: R$ {total:.2f}")

#Converter Celsius para F
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit:.1f}°F")

#Media
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Média: {media:.2f}")

#Idade em meses
ano_nascimento = int(input("Digite seu ano de nascimento: "))
mes_nascimento = int(input("Digite seu mês de nascimento (1-12): "))
idade_anos = 2026 - ano_nascimento
idade_meses = (idade_anos * 12) + (3 - mes_nascimento)  # março = mês 3 de 2026
print(f"Você tem aproximadamente {idade_meses} meses de vida.")

#Preço por kilo
peso = float(input("Digite o peso do produto em kg: "))
preco_por_kg = float(input("Digite o preço por kg (R$): "))
total = peso * preco_por_kg
print(f"Preço total: R$ {total:.2f}")