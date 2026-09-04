soma = 0
contador = 0

while contador < 10:
    valor = int(input("Digite um número: "))
    if valor % 6 == 0:
        soma = soma + valor
        contador = contador + 1

print(f"A soma dos 10 valores divisíveis por 6 é: {soma}")