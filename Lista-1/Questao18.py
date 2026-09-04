tensao = float(input("Digite a tensão de funcionamento (em Volts): "))
corrente = float(input("Digite a corrente elétrica consumida (em Ampères): "))

potencia = tensao * corrente

print(f"A potência do equipamento é: {potencia:.2f} W")