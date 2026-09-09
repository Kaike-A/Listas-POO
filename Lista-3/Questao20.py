memoria_utilizada = []
soma = 0

for i in range(5):
    memoria = float(input(f"Digite a quantidade de memória do teste {i+1}: "))
    memoria_utilizada.append(memoria)
    soma = soma + memoria

print(f"\nA soma de todos os valores de memória registrados é: {soma}")