vogais_lista = "aeiou"
quantidade_vogais = 0
quantidade_consoantes = 0

for i in range(10):
    letra = input(f"Digite a {i+1}ª letra: ").lower()
    
    if letra in vogais_lista:
        quantidade_vogais += 1
    else:
        quantidade_consoantes += 1

print(f"\nQuantidade de vogais: {quantidade_vogais}")
print(f"Quantidade de consoantes: {quantidade_consoantes}")