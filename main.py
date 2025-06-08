import os

opcoes_menu = ["Adicionar tarefa", "Visualizar tarefas", "Remover tarefa"]
lista_de_tarefas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def retornar_ao_menu_principal():

    while True:
        resposta = input("\nDeseja retornar ao menu principal? (S/N): ").upper().strip()

        if resposta in ["S", "N"]:
            limpar_tela()
            break

    if resposta == "S":
        executar_programa()

    # adicionar um else para encerrar o programa

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

    print(f"{'Índice'} | {'Tarefa'.ljust(50)} | {'Status'}")

    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{str(i).ljust(6)} | {tarefa['titulo'].ljust(50)} | {tarefa['status']}")  

    # retornar_ao_menu_principal()      
def remover_tarefa():    
    
    limpar_tela()

    visualizar_tarefas()

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

    lista_de_tarefas.pop(indice_corrigido)

def executar_programa():
    exibir_titulo()
    exibir_menu()
    opcao_selecionada = selecionar_opcao()

    if opcao_selecionada == 1:
        adicionar_tarefa()
    if opcao_selecionada == 2:
        visualizar_tarefas()
        retornar_ao_menu_principal() 
    if opcao_selecionada == 3:
        remover_tarefa()
        
        retornar_ao_menu_principal() 
    print("Encerrando o programa.")

if __name__ == "__main__":
    executar_programa()