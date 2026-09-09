continuar = 's'

while continuar.lower() == 's':
    print("\n--- Conversor de Temperatura ---")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    
    opcao = input("Escolha a opção (1-4): ")
    temp = float(input("Digite a temperatura: "))
    
    if opcao == '1':
        resultado = (temp * 9/5) + 32
        print(f"Resultado: {resultado:.2f} °F")
    elif opcao == '2':
        resultado = (temp - 32) * 5/9
        print(f"Resultado: {resultado:.2f} °C")
    elif opcao == '3':
        resultado = temp + 273.15
        print(f"Resultado: {resultado:.2f} K")
    elif opcao == '4':
        resultado = temp - 273.15
        print(f"Resultado: {resultado:.2f} °C")
    else:
        print("Opção inválida!")
        
    continuar = input("\nDeseja realizar uma nova conversão? (s/n): ")