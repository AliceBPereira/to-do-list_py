# Meu Gerenciador de Tarefas Pessoal

Um gerenciador de tarefas simples, porém eficaz, desenvolvido em Python para ajudar a organizar o seu dia a dia. Este projeto foi criado como parte do meu portfólio para demonstrar minhas habilidades em Python e desenvolvimento de aplicações de linha de comando.
**Importante:** Este projeto foi desenvolvido com base no tutorial/videoaula [Primeiro Projeto Python – FÁCIL para INICIANTES | Cirando uma To-Do List para Linha de Comando](https://youtu.be/AdLVm1z8x5A). O objetivo principal foi aprender e aplicar os conceitos apresentados.

---
## Funcionalidades Principais

* Adicionar novas tarefas
* Listar tarefas pendentes
* Marcar tarefas como concluídas
* Remover tarefas
* Interface de linha de comando intuitiva

---
## Tecnologias Utilizadas

* **Python 3:** Linguagem principal do projeto.
* **argparse:** Módulo Python para criar interfaces de linha de comando amigáveis.

---
## Como Executar

1.  **Clone o repositório (se aplicável):**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
2.  **Certifique-se de ter o Python 3 instalado.**
3.  **Execute o script `main.py` através da linha de comando:**

    Para **adicionar** uma nova tarefa:
    ```bash
    py main.py adicionar "Estudar bibliotecas de linha de comando2" "PROCURAR alternativas para o argparser2" "20/06/2025"
    ```

    Para **listar** todas as tarefas:
    ```bash
    py main.py listar
    ```

    Para **marcar uma tarefa como concluída** (substitua `ID_DA_TAREFA` pelo ID real):
    ```bash
    py main.py concluir ID_DA_TAREFA
    ```

    Para **remover uma tarefa** (substitua `ID_DA_TAREFA` pelo ID real):
    ```bash
    py main.py remover ID_DA_TAREFA
    ```
   
    Para **ver as opções de ajuda** e todos os comandos disponíveis:
    ```bash
    py main.py --ajuda
    ```
    
---
## Implementado 

* **Alice Barros Pereira**

---
## Licença

Este projeto é apenas para fins de demonstração e portfólio. Sinta-se à vontade para usá-lo como inspiração!

