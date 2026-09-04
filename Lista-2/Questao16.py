notas_estudantes = {
    "João": 8.5,
    "Maria": 6.0,
    "Pedro": 7.0,
    "Ana": 9.2
}

for nome, nota in notas_estudantes.items():
    if nota >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    print(f"Nome: {nome} | Nota: {nota:.1f} | Situação: {situacao}")