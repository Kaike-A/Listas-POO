numero = int(input("Digite um número inteiro não negativo: "))
fatorial = 1

if numero >= 0:
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print(f"O fatorial de {numero} é: {fatorial}")
else:
    print("Por favor, informe um número positivo.")