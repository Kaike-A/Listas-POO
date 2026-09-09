equipamentos = []
maior_preco = 0
nome_mais_caro = ""

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º equipamento: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    
    equipamentos.append((nome, preco))
    
    if preco > maior_preco:
        maior_preco = preco
        nome_mais_caro = nome

print("\n--- Equipamentos Cadastrados ---")
for nome, preco in equipamentos:
    print(f"- {nome}: R$ {preco:.2f}")

print(f"\nO equipamento mais caro é: {nome_mais_caro} (R$ {maior_preco:.2f})")