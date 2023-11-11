class Usuario:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
        self.projetos = []  # Adicionar uma lista de projetos ao usuário

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    @staticmethod
    def listar_funcoes_usuario():
        funcoes = {
            1: "Administrador",
            2: "Coordenador",
            3: "Analista",
            4: "Assistente",
            5: "Usuário"
        }
        return funcoes

# Para listar as funções de usuário, use a classe diretamente
funcoes_usuario = Usuario.listar_funcoes_usuario()