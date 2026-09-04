tensao = float(input("Digite a tensão fornecida (em Volts): "))
resistencia = float(input("Digite a resistência do circuito (em Ohms): "))

corrente = tensao / resistencia

print(f"A corrente elétrica resultante é: {corrente:.2f} A")