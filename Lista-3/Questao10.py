menor_latencia = float('inf')

for i in range(10):
    latencia = float(input(f"Digite a {i+1}ª latência (em ms): "))
    if latencia < menor_latencia:
        menor_latencia = latencia

print(f"\nA menor latência registrada foi: {menor_latencia} ms")