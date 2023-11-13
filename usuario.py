#Classe usuario
class Usuario:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    @staticmethod
    def listar_usuarios(usuarios):
        print("Usuários Disponíveis:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario.nome} - {usuario.funcao}")
        return usuarios

    @staticmethod
    def from_dict(dados):
        nome = dados["nome"]
        funcao = dados["funcao"]
        usuario = Usuario(nome, funcao)
        return usuario
    

    def to_dict(self):
        return {
            "nome": self.nome,
            "funcao": self.funcao
        }
        
    def listar_funcoes_usuario():
        funcoes = {
            1: "Administrador",
            2: "Coordenador",
            3: "Analista",
            4: "Assistente",
            5: "Usuário"
        }
        return funcoes
    
    def from_dict(dados):
        nome = dados["nome"]
        funcao = dados["funcao"]
        return Usuario(nome, funcao)

    def to_dict(self):
        return {
            "nome": self.nome,
            "funcao": self.funcao
        }
