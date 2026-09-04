notas = []
while len(notas) < 5:
    try:
        nota = float(input(f"Digite a {len(notas) + 1}ª nota: "))
        notas.append(nota)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

print(f"\nTodas as notas: {notas}")

media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")

maior_nota = max(notas)
print(f"Maior nota: {maior_nota}")

menor_nota = min(notas)
print(f"Menor nota: {menor_nota}")