from avl_tree import ArvoreAVL
from animal import Animal, Historico, Registro
import sys
import json

def consultar_animal(arvore, chave):
    node = arvore.consultar(chave)
    if node:
        print("")
        print("Animal encontrado:")
        node.animal.print_info()
    input("Pressione Enter para continuar...")  

def adicionar_animal(arvore):
    id = int(input("Digite o ID do animal: "))
    while arvore.consultar(id):
        print("")
        print("Animal com ID já existe. Por favor, escolha outro ID.")
        id = input("Digite o ID do animal: ")

    apelido = input("Digite o apelido do animal: ")
    inicio_monitoramento = input("Digite a data de início do monitoramento do animal: ")
    especie = input("Digite a espécie do animal: ")
    sexo = input("Digite o sexo do animal: ")
    data_nascimento = input("Digite a data de nascimento do animal: ")

    print("")
    add_history = input("Deseja adicionar um registro no histórico? (S/N): ")
    if add_history.lower() == "s":
        data_avaliacao = input("Digite a data da avaliação: ")
        temperatura = input("Digite a temperatura: ")
        peso = input("Digite o peso: ")
        altura = input("Digite a altura: ")
        amostra = input("Digite a amostra: ")
        exame = input("Digite o exame: ")
        problema = input("Digite o problema: ")
        registro = Registro(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
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
        historico = input("Deseja atualizar o histórico? (S/N): ")
        if historico.lower() == "s":
            data_avaliacao = input("Digite a data da avaliação: ")
            temperatura = input("Digite a temperatura: ")
            peso = input("Digite o peso: ")
            altura = input("Digite a altura: ")
            amostra = input("Digite a amostra: ")
            exame = input("Digite o exame: ")
            problema = input("Digite o problema: ")

            registro = Registro(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
            node.animal.addLog(registro)

def salvar_alteracoes(arvore, file_path):
    with open("./fauna2.json", 'w') as file:
        animals = []

        for node in arvore:
            animals.append(node.animal)

        json.dump({"animals": [a.to_dict() for a in animals]}, file, indent=4)

def sair():
    print("Saindo...")
    exit()

def menu(file_path):
    arvore = ArvoreAVL()

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

            # Cria um objeto Historico com as informações
            historico_info = animal['historico']
            for log in historico_info:
                data_avaliacao = log['data_avaliacao']
                temperatura = log['temperatura']
                peso = log['peso']
                altura = log['altura']
                amostra = log['amostra']
                exame = log['exame']
                problema = log['problema_saude']

                log = Registro(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
                historico.addLog(log)

            # Cria um objeto Animal com as informações
            animal = Animal(id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico)
            animal.print_info()

            # # Insere o objeto Animal na árvore AVL
            arvore.inserir(animal)

    while True:
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
            consultar_animal(arvore, int(input("Digite o ID do animal: "))) # OK
        elif choice == "2":
            adicionar_animal(arvore) # OK?
        elif choice == "3":
            remover_animal(arvore, int(input("Digite o ID do animal: "))) # OK
        elif choice == "4":
            adicionar_registro(arvore, int(input("Digite o ID do animal: "))) # OK?
        elif choice == "5":
            salvar_alteracoes(arvore, file_path)
        elif choice == "6":
            sair()
        else:
            print("Escolha inválida. Por favor, tente novamente.")


# Verifica se o caminho do arquivo foi passado como argumento
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = input("Digite o caminho do arquivo: ")

# Chama a função menu com o caminho do arquivo
menu(file_path)
