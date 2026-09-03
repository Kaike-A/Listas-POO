valor_emprestado = float(input("Digite o valor emprestado: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
meses = int(input("Digite a quantidade de meses: "))

juros_pagos = valor_emprestado * taxa_juros * meses
montante_total = valor_emprestado + juros_pagos

print(f"Valor dos juros pagos: R$ {juros_pagos:.2f}")
print(f"Montante total a ser pago: R$ {montante_total:.2f}")

# Comece misturando 3 ovos, 2 xícaras de açúcar e 3 colheres
# de sopa de manteiga até obter uma mistura homogênea. Em seguida, acrescente
# 1 xícara de leite e misture bem. Adicione aos poucos 3 xícaras de farinha
# de trigo e 1 colher de sopa de fermento em pó, mexendo delicadamente até
# formar uma massa uniforme. Despeje a massa em uma forma untada e enfarinhada
# e leve ao forno preaquecido a 180 graus por aproximadamente 35 a 40 minutos,
# ou até que o bolo esteja dourado e, ao espetar um palito no centro, ele saia
# limpo. Retire do forno, espere esfriar um pouco e sirva.