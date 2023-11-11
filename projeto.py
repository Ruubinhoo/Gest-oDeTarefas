class Projeto:
    Status_Disponiveis = ["Iniciado", "Em Andamento", "Finalizado"]

    def __init__(self, nome, descricao, status, prioridade, data_entrega, responsavel):
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.data_entrega = data_entrega
        self.responsavel = responsavel
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)