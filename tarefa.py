class Tarefa:
    def __init__(self, descricao, status, prioridade=None, data_entrega=None, responsavel=None):
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.data_entrega = data_entrega
        self.responsavel = responsavel

    def set_prioridade(self, prioridade):
        self.prioridade = prioridade

    def set_data_entrega(self, data_entrega):
        self.data_entrega = data_entrega

    def set_responsavel(self, responsavel):
        self.responsavel = responsavel