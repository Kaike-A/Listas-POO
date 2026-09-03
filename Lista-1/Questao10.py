valor_financiamento = float(input("Digite o valor do financiamento: "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): ")) / 100
quantidade_meses = int(input("Digite a quantidade de meses do financiamento: "))

montante = valor_financiamento * (1 + juros_mensal) ** quantidade_meses
juros_acumulados = montante - valor_financiamento

print(f"Montante final: R$ {montante:.2f}")
print(f"Juros acumulados: R$ {juros_acumulados:.2f}")