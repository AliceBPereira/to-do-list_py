import argparse
from gerenciador import GerenciadorDeTarefas

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Tarefas CLI em python")
    aubparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    # Subcomando para adicionar tarefa
    parser_adicionar = aubparsers.add_parser("adicionar", help="Adicionar uma nova tarefa")
    parser_adicionar.add_argument("titulo", type=str, help="Título da tarefa")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")
    parser_adicionar.add_argument("data_vencimento", type=str, help="Data de vencimento (dd/mm/yyyy)")

    # Subcomando para listar tarefas
    parser_listar = aubparsers.add_parser("listar", help="Listar tarefas")
    parser_listar.add_argument("--status", type=str, choices=["Pendente", "Concluída"], help="Filtrar por status")

    # Subcomando para editar tarefa
    parser_editar = aubparsers.add_parser("editar", help="Editar uma tarefa existente")
    parser_editar.add_argument("indice", type=int, help="Índice da tarefa a ser editada ")
    parser_editar.add_argument("--titulo", type=str, help="Novo título da tarefa")
    parser_editar.add_argument("--descricao", type=str, help="Nova descrição da tarefa")
    parser_editar.add_argument("--data_vencimento", type=str, help="Nova data de vencimento (dd/mm/yyyy)")

    # Subcomando para remover tarefa
    parser_remover = aubparsers.add_parser("remover", help="Remover uma tarefa")
    parser_remover.add_argument("indice", type=int, help="Índice da tarefa a ser removida")

    # Subcomando para marcar tarefa como concluída
    parser_concluir = aubparsers.add_parser("concluir", help="Marcar uma tarefa como concluída")
    parser_concluir.add_argument("indice", type=int, help="Índice da tarefa a ser marcada como concluída")

    args = parser.parse_args()
    gerenciador = GerenciadorDeTarefas("tarefas.pkl")

    if args.comando == "adicionar":
        gerenciador.adicionar_tarefa(args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "listar":
        gerenciador.listar_tarefas(args.status)
    elif args.comando == "editar":
        gerenciador.editar_tarefa(args.indice - 1, args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "remover":
        gerenciador.remover_tarefa(args.indice - 1)
    elif args.comando == "concluir":
        gerenciador.marcar_concluida(args.indice - 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# gerenciador = GerenciadorDeTarefas("teste.pkl")

# # gerenciador.adicionar_tarefa("Estudar Python", "Revisar conceitos de OOP", "2023-10-31")
# # gerenciador.editar_tarefa(0, titulo="Estudar Python Avançado", descricao="Revisar conceitos de OOP e Decoradores", data_vencimento="27/10/2024")
# # gerenciador.remover_tarefa(0)
# gerenciador.marcar_concluida(0)
# gerenciador.listar_tarefas()


