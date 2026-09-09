inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

multiplos = 0

for i in range(inicio, fim + 1):
    if i % 7 == 0:
        multiplos = multiplos + 1

print(f"\nA quantidade de códigos múltiplos de 7 é: {multiplos}")