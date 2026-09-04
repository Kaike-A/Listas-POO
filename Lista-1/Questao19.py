potencia = float(input("Digite a potência elétrica (em Watts): "))
tensao = float(input("Digite a tensão de funcionamento (em Volts): "))

corrente = potencia / tensao

print(f"A corrente elétrica aproximada é: {corrente:.2f} A")