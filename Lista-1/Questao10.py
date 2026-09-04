valor_financiamento = float(input("Digite o valor do financiamento: "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): ")) / 100
quantidade_meses = int(input("Digite a quantidade de meses do financiamento: "))

juros_acumulados = valor_financiamento * juros_mensal * quantidade_meses
montante_total = valor_financiamento + juros_acumulados

print(f"Juros acumulados: R$ {juros_acumulados:.2f}")
print(f"Montante total: R$ {montante_total:.2f}")