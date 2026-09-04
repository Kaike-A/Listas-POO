notas = []

quantidade = int(input("Quantas notas deseja inserir? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

try:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
except ZeroDivisionError:
    print("Erro: A lista está vazia, não é possível calcular a média (divisão por zero).")