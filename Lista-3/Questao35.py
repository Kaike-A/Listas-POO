# O setor de TI precisa de um sistema simples para gerenciar os equipamentos enviados para manutenção. Para cada equipamento,
# deverão ser armazenados o nome e o custo estimado do reparo.
# Desenvolva um programa em Python que implemente as operações de um CRUD (Create, Read, Update e Delete), permitindo ao usuário:

# - Cadastrar um novo equipamento e seu custo estimado de reparo;
# - Listar todos os equipamentos cadastrados e seus respectivos custos;
# - Atualizar os dados de um equipamento já cadastrado:
# - Excluir um equipamento do cadastro;
# - Identificar e exibir o equipamento que possui o maior custo estimado de reparo.

equipamentos = {}

while True:
    print('\n1.Cadastrar \n2.Listar \n3.Atualizar \n4.Excluir \n5.Mais caro \n6.Sair\n')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do equipamento: ')
        custo = float(input('Custo do reparo: R$ '))
        equipamentos[nome] = custo

    elif opcao == '2':
        for nome, custo in equipamentos.items():
            print(f'- {nome}: R$ {custo}')

    elif opcao == '3':
        nome = input('Qual o equipamento deseja atualizar? ')
        if nome in equipamentos:
            equipamentos[nome] = float(input('Novo custo: R$ '))

    elif opcao == '4':
        nome = input('Qual equipamento deseja excluir? ')
        if nome in equipamentos:
            del equipamentos[nome]

    elif opcao == '5':
        mais_caro = max(equipamentos, key=equipamentos.get)
        print(f'O mais caro é {mais_caro} custando R$ {equipamentos[mais_caro]}')

    elif opcao == '6':
        break