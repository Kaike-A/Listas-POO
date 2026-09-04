quadrados = {}

for i in range(1, 11):
    quadrados[i] = i * i

for chave, valor in quadrados.items():
    print(f"{chave}: {valor}")
    