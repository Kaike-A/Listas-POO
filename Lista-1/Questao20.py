nome = input("Digite o nome do participante: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"\nNome: {nome}")
print(f"Idade: {idade} anos")

if idade >= 18:
    print("Situação de acesso: Pode entrar normalmente.")
else:
    print("Situação de acesso: Precisa estar acompanhado por um responsável.")