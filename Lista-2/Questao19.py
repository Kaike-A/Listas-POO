estudantes = {
    "João": {"Nota 1": 8.0, "Nota 2": 7.5, "Média": 7.75},
    "Maria": {"Nota 1": 6.0, "Nota 2": 5.0, "Média": 5.5},
    "Kaike": {"Nota 1": 9.0, "Nota 2": 8.5, "Média": 8.75}
}

for nome, dados in estudantes.items():
    situacao = "Aprovado" if dados["Média"] >= 7.0 else "Reprovado"
    
    print(f"Aluno: {nome}")
    print(f"Nota 1: {dados['Nota 1']}")
    print(f"Nota 2: {dados['Nota 2']}")
    print(f"Média: {dados['Média']}")
    print(f"Situação: {situacao}\n")