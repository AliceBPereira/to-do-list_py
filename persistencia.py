import pickle

def salvar_tarefas(tarefas, nome_arquivo="tarefas.pkl"):
    """Salva a lista de tarefas em um arquivo usando pickle."""
    with open(nome_arquivo, "wb") as arquivo:
        pickle.dump(tarefas, arquivo)
    print(f"Tarefas salvas em '{nome_arquivo}' com sucesso!")

def carregar_tarefas(nome_arquivo="tarefas.pkl"):

    try:
        with open(nome_arquivo, "rb") as arquivo:
            tarefas = pickle.load(arquivo)
        print(f"Tarefas carregadas de '{nome_arquivo}' com sucesso!")
        return tarefas
    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Retornando lista vazia.")
        return []
    
    except EOFError:
        print(f"Arquivo '{nome_arquivo}' está vazio. Retornando lista vazia.")
        return []
    