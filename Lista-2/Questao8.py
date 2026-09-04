notas = [5.5, 7.0, 8.5, 4.0, 9.2, 6.8, 7.5, 10.0, 6.0, 7.1]
aprovados = 0

for nota in notas:
    if nota >= 7.0:
        aprovados = aprovados + 1

print(f"Quantidade de estudantes aprovados: {aprovados}")