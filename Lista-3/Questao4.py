softwares = ["Windows", "Office", "Chrome", "Python", "VS Code"]
print(f"Lista original: {softwares}")

novo_software = input("Digite o nome do novo software: ")
softwares.append(novo_software)

del softwares[1]

print(f"Lista atualizada: {softwares}")