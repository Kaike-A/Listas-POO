agenda = {}

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º contato: ")
    telefone = input(f"Digite o telefone de {nome}: ")
    agenda[nome] = telefone

nome_busca = input("\nDigite o nome que deseja buscar na agenda: ")

if nome_busca in agenda:
    print(f"Telefone: {agenda[nome_busca]}")
else:
    print("Contato não encontrado.")