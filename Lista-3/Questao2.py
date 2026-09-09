def calcular_valores(v1, v2):
    produto = v1 * v2
    if produto <= 1000:
        return produto
    else:
        return v1 + v2

resultado = calcular_valores(50, 25)
print(f"Resultado do processamento: {resultado}")