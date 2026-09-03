inventario = {
    "10001": {
        "Equipamento": "Computador Desktop",
        "Marca": "Dell",
        "Situação": "Funcionando"
    },
    "10002": {
        "Equipamento": "Projetor",
        "Marca": "Epson",
        "Situação": "Em manutenção"
    },
    "10003": {
        "Equipamento": "Monitor",
        "Marca": "Samsung",
        "Situação": "Funcionando"
    }
}

for patrimonio, informacoes in inventario.items():
    print(f"\nPatrimônio: {patrimonio}")
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")