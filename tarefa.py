from datetime import datetime #controla data de vencimento

class Tarefa:
    # construtor
    def __init__(self, titulo, descricao,data_vencimento, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y") # Converte a string para um objeto datetime
        self.status = status

    # Diferença de string e representation. string é o que aparece quando chamamos a função str() e representation é o que aparece quando chamamos a função repr()
    def __repr__(self ):
        return f"Tarefa(titulo='(self.titulo)', descricao='(self.descricao)', " \
               f"data_vencimento='(self.data_vencimento.strftime('%d/%m/%Y'))', status='(self.status)')"
    
    def marcar_como_concluida(self):
        # Marca a tarefa como concluída
        self.status = 'Concluída'
    
    def esta_atrasada(self):
        # Verifica se a data de vencimento é menor que a data atual
        return datetime.now() > self.data_vencimento and self.status == 'Pendente'
    
    def editar_titulo(self, titulo):
        # Edita o título da tarefa
        self.titulo = titulo

    def editar_descricao(self, descricao):
        # Edita a descrição da tarefa
        self.descricao = descricao

    def editar_data_vencimento(self, data_vencimento):
        # Edita a data de vencimento da tarefa
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")


    def detalhes(self):
        status = "Atrasada" if self.esta_atrasada() else self.status
        return (f"Título: {self.titulo}\n"
                f"Descrição: {self.descricao}\n"
                f"Data de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n"
                f"Status: {self.status}")