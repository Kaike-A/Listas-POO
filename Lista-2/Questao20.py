def exibir_nome_do_programa():
    """Exibe o nome do sistema de forma destacada."""
    print("\n--- Sistema de Gerenciamento Acadêmico ---\n")

def exibir_menu():
    """Apresenta as opções disponíveis no sistema."""
    print("SISTEMA ACADÊMICO")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Alterar situação")
    print("0 - Sair")

def cadastrar_estudante():
    """Simula o cadastro de um estudante."""
    print("Opção Cadastrar estudante selecionada.")

def listar_estudantes():
    """Simula a listagem de estudantes cadastrados."""
    print("Opção Listar estudantes selecionada.")

def alterar_situacao_estudante():
    """Simula a alteração da situação de um estudante."""
    print("Opção Alterar situação selecionada.")

def opcao_invalida():
    """Informa que a opção digitada não existe."""
    print("Opção escolhida inválida.")

def finalizar_programa():
    """Exibe a mensagem de encerramento do sistema."""
    print("Sistema sendo encerrado...")

def main():
    """
    Função principal responsável por coordenar a execução do programa,
    exibir menus e direcionar para as funções corretas conforme escolha.
    """
    exibir_nome_do_programa()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_estudante()
        elif opcao == '2':
            listar_estudantes()
        elif opcao == '3':
            alterar_situacao_estudante()
        elif opcao == '0':
            finalizar_programa()
            break
        else:
            opcao_invalida()
        print("-" * 20)

main()