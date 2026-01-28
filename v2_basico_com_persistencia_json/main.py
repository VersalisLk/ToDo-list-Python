
import json




##Funções ===============================================

def AdicionarTarefa(tarefas, titulo):
    tarefa = {
        'Titulo': titulo,
        'Concluida': False
    }
    tarefas.append(tarefa)


def ListarTarefas(tarefas):
    if not tarefas:
        print('A lista está vazia.')
    else:
        print('Tarefas: \n')
        for indice, task in enumerate(tarefas, start = 1 ):
            status = 'X' if task['Concluida'] else ' '
            print(f"{indice} - [{status}] {task['Titulo']}")


def ConcluirTarefa(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para ser concluida.')
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa['Titulo']}")
        
        
        try:
            num = int(input('Digite o número da tarefa concluida: '))
            
            if 1 <= num <= len(tarefas):
                tarefas[num-1]["Concluida"] = True
                print('Tarefa marcada como concluida!')
            else:
                print('Número inválido.')
        
        except ValueError:
            print('Digite apenas números')


def RemoverTarefa(tarefas):
    if not tarefas: 
        print('Não há tarefas a serem removidas.')
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa['Titulo']}")
        
        
        try:
        
            num = int(input('Selecione a tarefa que deseja remover: '))
        
            if 1 <= num <= len(tarefas):
                tarefas.pop(num-1)
                print('Tarefa Removida!')
            else:
                print('Número inválido.')
    
        except ValueError:
            print('Digite apenas números.')

def SalvarArquivo(tarefas):
        with open('Tarefas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def CarregarArquivo():
    try:
        with open('Tarefas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

##==========================================================

tarefas = CarregarArquivo()

##Main =====================================================
while True:
    print("\n==== TO DO LIST ====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Remover Tarefa")
    print("5 - Sair")

    try:
        op = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas números.')
        continue



    if op == 1:
        a = str(input('Digite uma tarefa: '))
        AdicionarTarefa(tarefas, a)
        SalvarArquivo(tarefas)
        print('\nTarefa adicionada com sucesso!')
    elif op == 2:
        ListarTarefas(tarefas)
    elif op == 3:
        ConcluirTarefa(tarefas)
        SalvarArquivo(tarefas)
    elif op == 4:
        RemoverTarefa(tarefas)
        SalvarArquivo(tarefas)
    elif op == 5:
        print('Saindo...')
        break
    else:
        print('Opção Inválida')



##========================================================
