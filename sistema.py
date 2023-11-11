import json
import os
from usuario import Usuario
from projeto import Projeto

class SistemaGerenciamentoProjetos:
    def __init__(self):
        self.usuarios = []
        self.projetos = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def salvar_dados(self, nome_arquivo):
        dados = {
            "usuarios": [usuario.to_dict() for usuario in self.usuarios],
            "projetos": [projeto.to_dict() for projeto in self.projetos]
        }

        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    def carregar_dados(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self.usuarios = [Usuario.from_dict(usuario) for usuario in dados["usuarios"]]
                self.projetos = [Projeto.from_dict(projeto) for projeto in dados["projetos"]]

    def listar_usuarios_disponiveis(self):
        return self.usuarios
