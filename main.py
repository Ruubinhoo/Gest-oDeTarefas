from usuario import Usuario
from tarefa import Tarefa
from projeto import Projeto
from sistema import SistemaGerenciamentoProjetos
import os

class Main:
    @staticmethod
    def main():
        sistema = SistemaGerenciamentoProjetos()
        funcoes_usuario = Usuario.listar_funcoes_usuario()
        dados_carregados = False
        

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


            if os.path.exists("dados.json"):
                sistema.carregar_dados("dados.json")
                dados_carregados = True
            
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
                for i, status in enumerate(Projeto.Status_Disponíveis, start=1):
                    print(f"{i}. {status}")
                numero_status_projeto = input("Status do Projeto: ")
                try:
                    numero_status_projeto = int(numero_status_projeto)
                    if 1 <= numero_status_projeto <= len(Projeto.Status_Disponíveis):
                        status_projeto = Projeto.Status_Disponíveis[numero_status_projeto - 1]

                        # Listar prioridades de projeto e permitir que o usuário escolha pelo número
                        print("Prioridades Disponíveis:")
                        for i, prioridade in enumerate(Projeto.prioridades_disponíveis, start=1):
                            print(f"{i}. {prioridade}")
                        numero_prioridade_projeto = input("Prioridade do projeto: ")
                        try:
                            numero_prioridade_projeto = int(numero_prioridade_projeto)
                            if 1 <= numero_prioridade_projeto <= len(Projeto.prioridades_disponíveis):
                                prioridade_projeto = Projeto.prioridades_disponíveis[numero_prioridade_projeto - 1]

                                data_entrega_projeto = input("Data de entrega do projeto: ")

                                # Liste os usuários disponíveis neste ponto
                                usuarios_disponíveis = sistema.listar_usuarios()
                                print("Usuários disponíveis:")
                                for i, user in enumerate(usuarios_disponíveis, start=1):
                                    print(f"{i}. {user.nome} - Função: {user.funcao}")

                                numero_usuario = input("Selecione um usuário responsável pelo projeto: ")

                                try:
                                    numero_usuario = int(numero_usuario)
                                    if 1 <= numero_usuario <= len(usuarios_disponíveis):
                                        responsável_usuario = usuarios_disponíveis[numero_usuario - 1]

                                        projeto = Projeto(nome_projeto, descricao, status_projeto, prioridade_projeto, data_entrega_projeto, responsável_usuario.nome)
                                        sistema.adicionar_projeto(projeto)
                                        print("Projeto adicionado com sucesso!")
                                    else:
                                        print("Usuário inválido.")
                                except ValueError:
                                    print("Número inválido.")

                            else:
                                print("Prioridade de projeto inválida.")
                        except ValueError:
                            print("Número inválido.")
                    else:
                        print("Status de projeto inválido.")
                except ValueError:
                    print("Número inválido.")

            elif opcao == '3':
                projetos_disponíveis = sistema.listar_projetos()
                numero_projeto = input("Selecione um projeto pelo número: ")
                projeto_selecionado = sistema.selecionar_projeto(numero_projeto)


                if projeto_selecionado:
                    sistema.adicionar_tarefa_a_projeto(projeto_selecionado)
                else:
                    print(f"Projeto não encontrado.")

            elif opcao == '4':
                Usuario.listar_usuarios(sistema.usuarios)
                if dados_carregados:
                    sistema.salvar_dados("dados.json")    

            elif opcao == '5':
                sistema.listar_projetos()
                if dados_carregados:
                    sistema.salvar_dados("dados.json")

            elif opcao == '6':
                projetos_disponíveis = sistema.listar_projetos()
                numero_projeto = input("Selecione um projeto pelo número: ")
                projeto_selecionado = sistema.selecionar_projeto(numero_projeto)

                if projeto_selecionado:
                    print("Status de Projeto Disponíveis:")
                    for i, status in enumerate(Projeto.Status_Disponíveis, start=1):
                        print(f"{i}. {status}")
                    numero_status_projeto = input("Status do Projeto: ")
                    try:
                        numero_status_projeto = int(numero_status_projeto)
                        if 1 <= numero_status_projeto <= len(Projeto.Status_Disponíveis):
                            status_projeto = Projeto.Status_Disponíveis[numero_status_projeto - 1]
                            projeto_selecionado.alterar_status(status_projeto)
                            print("Status do projeto alterado com sucesso!")
                        else:
                            print("Status de projeto inválido.")
                    except ValueError:
                        print("Número inválido.")
                else:
                    print(f"Projeto não encontrado.")

            elif opcao == '7':
                projetos_disponíveis = sistema.listar_projetos()
                numero_projeto = input("Selecione o PROJETO: ")
                projeto_selecionado = sistema.selecionar_projeto(numero_projeto)

                if projeto_selecionado:
                    tarefas_disponíveis = projeto_selecionado.tarefas
                    print("Tarefas disponíveis para o projeto:")
                    for i, tarefa in enumerate(tarefas_disponíveis, start=1):
                        print(f"{i}. Descrição da Tarefa: {tarefa.descricao} - Status: {tarefa.status}")
                    numero_tarefa = input("Selecione a TAREFA: ")
                    tarefa_selecionada = sistema.selecionar_tarefa(projeto_selecionado, numero_tarefa)

                    if tarefa_selecionada:
                        print(f"Status atual da Tarefa: {tarefa_selecionada.status}")
                        print("Selecione o novo status da Tarefa:")
                        for i, status in enumerate(Tarefa.status_tarefa_disponiveis, start=1):
                            print(f"{i}. {status}")
                        numero_status_tarefa = input("Novo Status da Tarefa: ")
                        try:
                            numero_status_tarefa = int(numero_status_tarefa)
                            if 1 <= numero_status_tarefa <= len(Tarefa.status_tarefa_disponiveis):
                                novo_status_tarefa = Tarefa.status_tarefa_disponiveis[numero_status_tarefa - 1]
                                tarefa_selecionada.alterar_status(novo_status_tarefa)
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
    Main.main()