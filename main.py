import os

opcoes_menu = ["Adicionar tarefa", "Visualizar tarefas", "Remover tarefa", "Sair"]
lista_de_tarefas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def retornar_ao_menu_principal():
    while True:
        resposta = input("\nDeseja retornar ao menu principal (S/N)? ").upper().strip()

        if resposta not in ["S", "N"]:
            print("\n[ERROR] - Entrada inválida")
        else:
            break
    
    if resposta == "N":
        limpar_tela()
        print("Encerrando programa")
        exit()        

    limpar_tela()

def exibir_titulo():
    titulo = "Bem-vindo ao Organizador de Tarefas"
    borda = "-"*len(titulo)
    
    print(borda)
    print(titulo)
    print(f"{borda}\n")
def exibir_menu():
    for i, opcao in enumerate(opcoes_menu, start=1):
        print(f"{i} - {opcao}")  
def selecionar_opcao():
    while True:
        try:
            opcoes_selecionada = int(input("\nO que deseja fazer? "))

            if opcoes_selecionada < 1 or opcoes_selecionada > len(opcoes_menu):
                print("\n[ERRO] Selecione uma opção válida")
            else:
                return opcoes_selecionada                
        except ValueError:
            print("\n[ERRO] Selecione uma opção válida")
def listar_tarefas():
    print(f"{'Índice'} | {'Tarefa'.ljust(50)} | {'Status'}")

    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{str(i).ljust(6)} | {tarefa['titulo'].ljust(50)} | {'✅' if tarefa['status'] else '❌'}")

def adicionar_tarefa():

    limpar_tela()

    titulo = input("Título da tarefa: ").capitalize().strip()

    tarefa = {
        "titulo":titulo,
        "status":False
    }

    lista_de_tarefas.append(tarefa)

    retornar_ao_menu_principal()
def visualizar_tarefas():

    limpar_tela()

    if not lista_de_tarefas:
        print("Não há tarefas registradas")
        retornar_ao_menu_principal()

    listar_tarefas()

    retornar_ao_menu_principal()
def remover_tarefa():    
    
    limpar_tela()

    listar_tarefas()

    while True:
        try:
            tarefa_selecionada = int(input("\nInforme o indice da tarefa para remover: "))
            if tarefa_selecionada < 1 or tarefa_selecionada > len(lista_de_tarefas):
                print("\n[ERRO] Selecione um índice válido")

            else:
                break    
        except ValueError:
            print("\n[ERRO] Selecione um índice válido")

    indice_corrigido = tarefa_selecionada - 1

    tarefa_removida = lista_de_tarefas.pop(indice_corrigido)

    mensagem_retorno = f"Tarefa: '{tarefa_removida['titulo']}' removida com sucesso"

    print("")    
    print(f"-"*len(mensagem_retorno))
    print(mensagem_retorno)
    print("-"*len(mensagem_retorno))

    retornar_ao_menu_principal()

while True:
    exibir_titulo()
    exibir_menu()
    opcao_selecionada = selecionar_opcao()

    if opcao_selecionada == 1:
        adicionar_tarefa()
    elif opcao_selecionada == 2:
        visualizar_tarefas()
    elif opcao_selecionada == 3:
        remover_tarefa()
    else:
        limpar_tela()
        print("Encerrando programa")
        break