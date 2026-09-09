valores_cpu = []

for i in range(7):
    valor = int(input(f"Digite o valor {i+1} de uso da CPU: "))
    valores_cpu.append(valor)

print("\nValores na ordem inversa:")
# range do último elemento até o primeiro (passo -1)
for i in range(6, -1, -1):
    print(valores_cpu[i])