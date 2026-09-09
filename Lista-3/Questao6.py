codigo1 = int(input("Digite o primeiro código: "))
codigo2 = int(input("Digite o segundo código: "))

inicio = min(codigo1, codigo2)
fim = max(codigo1, codigo2)

print(f"\nIdentificadores entre {inicio} e {fim}:")
for i in range(inicio, fim + 1):
    print(i)