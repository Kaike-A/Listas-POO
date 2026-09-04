disciplina = {
    "nome": "Introdução à Programação",
    "professor": "João Silva",
    "carga_horaria": 60,
    "periodo": "1º Semestre"
}

chave_buscada = input("Digite o nome de uma chave para buscar: ")

if chave_buscada in disciplina:
    print("A chave existe.")
else:
    print("A chave não foi encontrada.")