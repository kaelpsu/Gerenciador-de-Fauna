from avl_tree import ArvoreAVL
from animal import Animal, Historico, Registro
from ui import *
import json

def consultar_animal(arvore, chave):
    node = arvore.consultar(chave)
    if node:
        print("")
        print("Animal encontrado:")
        node.animal.print_info()
    input("Pressione Enter para continuar...")
    

def adicionar_animal(arvore):
    
    while True:
        id = solicita_id()
        
        if not arvore.consultar(id):
            break
        
        print("")
        print("Animal com ID já existente. Por favor, escolha outro ID.")

    apelido = solicita_apelido()

    inicio_monitoramento = solicita_data()

    especie = solicita_especie()

    sexo = solicita_sexo()

    data_nascimento = solicita_data_nascimento()

    print("")

    add_history = input("Deseja adicionar um registro no histórico? (S/N): ")
    
    if add_history.lower() == "s":
        registro = solicita_registro()

        historico = Historico([registro])
    else:

        historico = Historico([])


    animal = Animal(id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico)


    arvore.inserir(animal)

def remover_animal(arvore, chave):
    arvore.remover(chave)

def adicionar_registro(arvore, chave):
    node = arvore.consultar(chave)
    
    if node:
        print("")
        print("Animal encontrado. Informações atuais:")
        node.animal.print_info()

        print("")

        atualizar_historico = input("Deseja atualizar o histórico? (S/N): ")
        if atualizar_historico.lower() == "s":
            registro = solicita_registro()
            node.animal.add_log(registro)


def salvar_alteracoes(arvore, save_path):
    with open(save_path, 'w') as file:
        animals = []

        # Percorre todos os nós da árvore e adiciona os animais na lista
        for node in arvore:
            animals.append(node.animal)

        # Cria um dicionário com a lista de animais e escreve no arquivo JSON
        json.dump({"animals": [a.convert_to_dictionary() for a in animals]}, file, indent=4)

def sair():
    print("Saindo...")
    exit()
    
def display_menu(arvore):
    print("")
    arvore.inorder_traversal(arvore.raiz)
    print("")
    print("Menu:")
    print("1. Consultar animal")
    print("2. Adicionar animal")
    print("3. Remover animal")
    print("4. Adicionar registro")
    print("5. Salvar alterações")
    print("6. Sair")

    choice = input("Digite sua escolha: ")

    if choice == "1":
        consultar_animal(arvore, int(input("Digite o ID do animal: ")))
    elif choice == "2":
        adicionar_animal(arvore)
    elif choice == "3":
        remover_animal(arvore, int(input("Digite o ID do animal: ")))
    elif choice == "4":
        adicionar_registro(arvore, int(input("Digite o ID do animal: ")))
    elif choice == "5":
        save_path = input("Digite o caminho do arquivo para salvar as alterações: ")
        salvar_alteracoes(arvore, save_path)
    elif choice == "6":
        sair()
    else:
        print("Escolha inválida. Por favor, tente novamente.")

def initialize(file_path):
    arvore = ArvoreAVL()

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for animal in data['animals']:
                id = animal['id']
                apelido = animal['apelido']
                inicio_monitoramento = animal['inicio_monitoramento']
                especie = animal['especie']
                sexo = animal['sexo']
                data_nascimento = animal['data_nascimento']

                historico = Historico([])
                historico_info = animal['historico']
                for log in historico_info:
                    data_avaliacao = log['data_avaliacao']
                    temperatura = log['temperatura']
                    peso = log['peso']
                    altura = log['altura']
                    amostra = log['amostra']
                    exame = log['exame']
                    problema = log['problema_de_saude']

                    log = Registro(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
                    historico.add_log(log)

                animal = Animal(id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico)

                arvore.inserir(animal)
                
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        exit()

    while True:
        display_menu(arvore)