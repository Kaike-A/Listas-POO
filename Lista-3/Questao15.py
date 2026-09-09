soma = 0
quantidade = 0

# Maior que 0 e menor que 20 (portanto, de 2 até 18 em passos de 2)
for i in range(2, 20, 2):
    soma = soma + i
    quantidade = quantidade + 1

media = soma / quantidade
print(f"A média dos identificadores válidos é: {media}")