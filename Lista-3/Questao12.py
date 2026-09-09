soma = 0
quantidade = 0

while quantidade < 10:
    codigo = int(input(f"Digite o {quantidade+1}º código divisível por 3: "))
    
    if codigo % 3 == 0:
        soma = soma + codigo
        quantidade = quantidade + 1
    else:
        print("Erro: O código deve ser divisível por 3. Tente novamente.")

print(f"\nA soma dos códigos válidos é: {soma}")