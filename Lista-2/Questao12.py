# Crie um dicionário que associe os números de 1 a 10 aos seus respectivos quadrados.
# Em seguida, exiba todas as chaves e seus respectivos valores.

quadrados = {}

for i in range(1, 11):
    quadrados[i] = i * i

for chave, valor in quadrados.items():
    print(f'{chave}: {valor}')
    asojkfnasn