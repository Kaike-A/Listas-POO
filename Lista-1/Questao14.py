preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade adquirida: "))
desconto = float(input("Digite o valor do desconto (em R$): "))

valor_final = (preco_unitario * quantidade) - desconto

print(f"Valor final a ser pago: R$ {valor_final:.2f}")