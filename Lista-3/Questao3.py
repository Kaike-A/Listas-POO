menor_igual_100 = 0
maior_100 = 0
soma_latencias = 0
maior_latencia = -1

for i in range(10):
    latencia = float(input(f"Digite a latência do teste {i+1} (em ms): "))
    
    if latencia <= 100:
        menor_igual_100 += 1
    else:
        maior_100 += 1
        
    soma_latencias += latencia
    
    if latencia > maior_latencia:
        maior_latencia = latencia

media = soma_latencias / 10

print(f"\nTestes <= 100 ms: {menor_igual_100}")
print(f"Testes > 100 ms: {maior_100}")
print(f"Média das latências: {media:.2f} ms")
print(f"Maior latência: {maior_latencia:.2f} ms")