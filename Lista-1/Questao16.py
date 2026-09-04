tensao = float(input("Digite a tensão elétrica (em Volts): "))
corrente = float(input("Digite a corrente elétrica (em Ampères): "))

resistencia = tensao / corrente

print(f"A resistência elétrica do componente é: {resistencia:.2f} Ω")