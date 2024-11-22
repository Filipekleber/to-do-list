def adicionar_tarefa(tarefa):
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(tarefa + "\n")
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
            else:
                print("Nenhuma tarefa encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def remover_tarefa(numero):
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        if 1 <= numero <= len(tarefas):
            tarefa_removida = tarefas.pop(numero - 1).strip()
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(tarefas)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            try:
                numero = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(numero)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif escolha == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()