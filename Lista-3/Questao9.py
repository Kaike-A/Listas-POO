primeiro = int(input("Digite o primeiro identificador: "))
ultimo = int(input("Digite o último identificador: "))

soma = 0
quantidade = 0

for i in range(primeiro, ultimo + 1):
    soma = soma + i
    quantidade = quantidade + 1

media = soma / quantidade
print(f"\nA média dos identificadores é: {media}")