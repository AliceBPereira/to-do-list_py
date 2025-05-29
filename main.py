from tarefa import Tarefa
from persistencia import carregar_tarefas, salvar_tarefas

tarefa1 = Tarefa("Estudar Python", "Estudar a aula 2 de Python", "10/10/2025")


tarefa2 = Tarefa(titulo="Fazer compras", descricao="Comprar leite e pão", data_vencimento= "15/10/2024", status="Pendente")

salvar_tarefas([tarefa1, tarefa2], "tarefas.pkl")  # Salva as tarefas em um arquivo
tarefas = carregar_tarefas("tarefas.pkl")  # Carrega as tarefas do arquivo

print(tarefas[0].detalhes())  # Exibe os detalhes da primeira tarefa