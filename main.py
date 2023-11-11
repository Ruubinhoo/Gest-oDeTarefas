from usuario import Usuario
from tarefa import Tarefa
from projeto import Projeto
from sistema import SistemaGerenciamentoProjetos
import os

status_projeto_disponiveis = ["Iniciado", "Em Andamento", "Finalizado"]
status_tarefa_disponiveis = ["Iniciado", "Em Andamento", "Finalizado"]
prioridades_disponiveis = ["Baixa", "Média", "Alta"]

def listar_usuarios(sistema):
    print("Usuários Disponíveis:")
    for i, usuario in enumerate(sistema.usuarios, start=1):
        print(f"{i}. {usuario.nome} - {usuario.funcao}")
    return sistema.usuarios

def listar_projetos(sistema):
    print("Projetos Disponíveis:")
    for i, projeto in enumerate(sistema.projetos, start=1):
        print(f"{i}. {projeto.nome} - Responsável: {projeto.responsavel}")
        print(f"   Descrição do Projeto: {projeto.descricao}")
        print(f"   Status do Projeto: {projeto.status}")
        print(f"   Prioridade do Projeto: {projeto.prioridade}")
        print("   Tarefas:")
        for j, tarefa in enumerate(projeto.tarefas, start=1):
            print(f"    {j}. Descrição da Tarefa: {tarefa.descricao}")
            print(f"       Status da Tarefa: {tarefa.status}")
        print("   ___________________________________")
    return sistema.projetos

def selecionar_usuario(usuarios, numero_selecionado):
    try:
        numero_selecionado = int(numero_selecionado)
        if 1 <= numero_selecionado <= len(usuarios):
            return usuarios[numero_selecionado - 1]
        else:
            return None
    except ValueError:
        return None

def selecionar_projeto(projetos, numero_selecionado):
    try:
        numero_selecionado = int(numero_selecionado)
        if 1 <= numero_selecionado <= len(projetos):
            return projetos[numero_selecionado - 1]
        else:
            return None
    except ValueError:
        return None

def selecionar_tarefa(tarefas, numero_selecionado):
    try:
        numero_selecionado = int(numero_selecionado)
        if 1 <= numero_selecionado <= len(tarefas):
            return tarefas[numero_selecionado - 1]
        else:
            return None
    except ValueError:
        return None

def alterar_status_projeto(projeto, novo_status):
    projeto.status = novo_status

def alterar_status_tarefa(tarefa, novo_status):
    tarefa.status = novo_status

def adicionar_tarefa_a_projeto(projeto_selecionado):
    descricao_tarefa = input("Descrição da tarefa: ")

    # Listar status de tarefa e permitir que o usuário escolha pelo número
    print("Status de Tarefa Disponíveis:")
    for i, status in enumerate(status_tarefa_disponiveis, start=1):
        print(f"{i}. {status}")
    numero_status_tarefa = input("Status da tarefa: ")
    
    try:
        numero_status_tarefa = int(numero_status_tarefa)
        if 1 <= numero_status_tarefa <= len(status_tarefa_disponiveis):
            status_tarefa = status_tarefa_disponiveis[numero_status_tarefa - 1]
            
            tarefa = Tarefa(descricao_tarefa, status_tarefa)
            projeto_selecionado.adicionar_tarefa(tarefa)
            print("Tarefa adicionada ao projeto com sucesso!")
        else:
            print("Status de tarefa inválido.")
    except ValueError:
        print("Número inválido.")

def main():
    sistema = SistemaGerenciamentoProjetos()
    funcoes_usuario = Usuario.listar_funcoes_usuario()

    # Menu de opções
    while True:
        print("\n           Menu Principal")
        print("------------------------------------")
        print("|1. Adicionar Usuário              |")
        print("|2. Adicionar Projeto              |")
        print("|3. Adicionar Tarefa a um Projeto  |")
        print("|4. Listar Usuários                |")
        print("|5. Listar Projetos                |")
        print("|6. Alterar Status de Projeto      |")
        print("|7. Alterar Status de Tarefa       |")
        print("|8. Sair                           |")
        print("------------------------------------")
        opcao = input("Escolha uma Opção: ")

        if opcao == '1':
            nome = input("Nome do Usuário: ")
            for numero, funcao in funcoes_usuario.items():
                print(f"{numero}. {funcao}")
            
            numero_funcao = input("Função: ")
            try:
                numero_funcao = int(numero_funcao)
                if numero_funcao in funcoes_usuario:
                    funcao = funcoes_usuario[numero_funcao]
                    usuario = Usuario(nome, funcao)
                    sistema.adicionar_usuario(usuario)
                    print("------------------------------------")
                    print("Usuário adicionado com sucesso!")
                    input("Pressione Enter para continuar...")
                    os.system('cls')
                else:
                    print("Função inválida.")
            except ValueError:
                print("Número inválido.")
                

        elif opcao == '2':
            nome_projeto = input("Nome do projeto: ")
            descricao = input("Descrição do projeto: ")

            # Listar status de projeto e permitir que o usuário escolha pelo número
            print("Status de Projeto Disponíveis:")
            for i, status in enumerate(status_projeto_disponiveis, start=1):
                print(f"{i}. {status}")
            numero_status_projeto = input("Status do Projeto: ")
            try:
                numero_status_projeto = int(numero_status_projeto)
                if 1 <= numero_status_projeto <= len(status_projeto_disponiveis):
                    status_projeto = status_projeto_disponiveis[numero_status_projeto - 1]

                    # Listar prioridades de projeto e permitir que o usuário escolha pelo número
                    print("Prioridades Disponíveis:")
                    for i, prioridade in enumerate(prioridades_disponiveis, start=1):
                        print(f"{i}. {prioridade}")
                    numero_prioridade_projeto = input("Prioridade do projeto: ")
                    try:
                        numero_prioridade_projeto = int(numero_prioridade_projeto)
                        if 1 <= numero_prioridade_projeto <= len(prioridades_disponiveis):
                            prioridade_projeto = prioridades_disponiveis[numero_prioridade_projeto - 1]

                            data_entrega_projeto = input("Data de entrega do projeto: ")

                            usuarios_disponiveis = listar_usuarios(sistema)
                            numero_usuario = input("Selecione um usuário responsável pelo projeto: ")
                            responsavel_usuario = selecionar_usuario(usuarios_disponiveis, numero_usuario)

                            if responsavel_usuario:
                                projeto = Projeto(nome_projeto, descricao, status_projeto, prioridade_projeto, data_entrega_projeto, responsavel_usuario.nome)
                                sistema.adicionar_projeto(projeto)
                                print("Projeto adicionado com sucesso!")
                            else:
                                print("Usuário não encontrado ou não disponível como responsável. Projeto não adicionado.")
                        else:
                            print("Prioridade de projeto inválida.")
                    except ValueError:
                        print("Número inválido.")
                else:
                    print("Status de projeto inválido.")
            except ValueError:
                print("Número inválido.")

        elif opcao == '3':
            projetos_disponiveis = listar_projetos(sistema)
            numero_projeto = input("Selecione um projeto pelo número: ")
            projeto_selecionado = selecionar_projeto(projetos_disponiveis, numero_projeto)

            if projeto_selecionado:
                adicionar_tarefa_a_projeto(projeto_selecionado)
            else:
                print(f"Projeto não encontrado.")

        elif opcao == '4':
            listar_usuarios(sistema)

        elif opcao == '5':
            listar_projetos(sistema)

        elif opcao == '6':
            projetos_disponiveis = listar_projetos(sistema)
            numero_projeto = input("Selecione um projeto pelo número: ")
            projeto_selecionado = selecionar_projeto(projetos_disponiveis, numero_projeto)

            if projeto_selecionado:
                print("Status de Projeto Disponíveis:")
                for i, status in enumerate(status_projeto_disponiveis, start=1):
                    print(f"{i}. {status}")
                numero_status_projeto = input("Status do Projeto: ")
                try:
                    numero_status_projeto = int(numero_status_projeto)
                    if 1 <= numero_status_projeto <= len(status_projeto_disponiveis):
                        status_projeto = status_projeto_disponiveis[numero_status_projeto - 1]
                        alterar_status_projeto(projeto_selecionado, status_projeto)
                        print("Status do projeto alterado com sucesso!")
                    else:
                        print("Status de projeto inválido.")
                except ValueError:
                    print("Número inválido.")
            else:
                print(f"Projeto não encontrado.")

        elif opcao == '7':
            projetos_disponiveis = listar_projetos(sistema)
            numero_projeto = input("Selecione o PROJETO: ")
            projeto_selecionado = selecionar_projeto(projetos_disponiveis, numero_projeto)

            if projeto_selecionado:
                tarefas_disponiveis = projeto_selecionado.tarefas
                print("Tarefas disponíveis para o projeto:")
                for i, tarefa in enumerate(tarefas_disponiveis, start=1):
                    print(f"{i}. Descrição da Tarefa: {tarefa.descricao} - Status: {tarefa.status}")
                numero_tarefa = input("Selecione a TAREFA: ")
                tarefa_selecionada = selecionar_tarefa(tarefas_disponiveis, numero_tarefa)

                if tarefa_selecionada:
                    print(f"Status atual da Tarefa: {tarefa_selecionada.status}")
                    print("Selecione o novo status da Tarefa:")
                    for i, status in enumerate(status_tarefa_disponiveis, start=1):
                        print(f"{i}. {status}")
                    numero_status_tarefa = input("Novo Status da Tarefa: ")
                    try:
                        numero_status_tarefa = int(numero_status_tarefa)
                        if 1 <= numero_status_tarefa <= len(status_tarefa_disponiveis):
                            novo_status_tarefa = status_tarefa_disponiveis[numero_status_tarefa - 1]
                            alterar_status_tarefa(tarefa_selecionada, novo_status_tarefa)
                            print("Status da tarefa alterado com sucesso!")
                        else:
                            print("Status de tarefa inválido.")
                    except ValueError:
                        print("Número inválido.")
                else:
                    print("Tarefa não encontrada.")

        elif opcao == '8':
            print("Saindo do programa.")
            break

if __name__ == "__main__":
    main()