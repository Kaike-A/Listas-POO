maior_valor = -1

for i in range(15):
    utilizacao = float(input(f"Digite a utilização do processador no período {i+1}: "))
    if utilizacao > maior_valor:
        maior_valor = utilizacao

print(f"\nO maior valor observado foi: {maior_valor}")