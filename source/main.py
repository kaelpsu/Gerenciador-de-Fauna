from avl_tree import ArvoreAVL
from animal import Animal, Historico
import sys

def consultar_registro(arvore, chave):
    node = arvore.consultar(chave)
    if node:
        print("Animal encontrado:")
        node.animal.print_info()
    input("Pressione Enter para continuar...")  

def adicionar_registro(arvore):
    id = input("Digite o ID do animal: ")
    while arvore.busca(id):
        print("Animal com ID já existe. Por favor, escolha outro ID.")
        id = input("Digite o ID do animal: ")

    apelido = input("Digite o apelido do animal: ")
    inicio_monitoramento = input("Digite a data de início do monitoramento do animal: ")
    especie = input("Digite a espécie do animal: ")
    sexo = input("Digite o sexo do animal: ")
    data_nascimento = input("Digite a data de nascimento do animal: ")

    add_history = input("Deseja adicionar o histórico? (S/N): ")
    if add_history.lower() == "s":
        data_avaliacao = input("Digite a data da avaliação: ")
        temperatura = input("Digite a temperatura: ")
        peso = input("Digite o peso: ")
        altura = input("Digite a altura: ")
        amostra = input("Digite a amostra: ")
        exame = input("Digite o exame: ")
        problema = input("Digite o problema: ")
        historico = Historico(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
    else:
        historico = None

    animal = Animal(id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico)

    arvore.inserir(animal)

def remover_registro(arvore, chave):
    arvore.remover(chave)

def atualizar_registro(arvore, chave):
    node = arvore.consultar(chave)
    if node:
        print("Animal encontrado. Informações atuais:")
        node.animal.print_info()

        historico = input("Deseja atualizar o histórico? (S/N): ")
        if historico.lower() == "s":
            data_avaliacao = input("Digite a data da avaliação: ")
            temperatura = input("Digite a temperatura: ")
            peso = input("Digite o peso: ")
            altura = input("Digite a altura: ")
            amostra = input("Digite a amostra: ")
            exame = input("Digite o exame: ")
            problema = input("Digite o problema: ")
            node.animal.historico = Historico(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)

def salvar_alteracoes(arvore, file_path):
    with open(file_path, 'w') as file:
        for node in arvore:
            animal = node.animal
            line = f"{animal.id},{animal.apelido},{animal.inicio_monitoramento},{animal.especie},{animal.sexo},{animal.data_nascimento}"
            historico_info = [str(h) for h in animal.historico.get_info()]
            line += "," + ",".join(historico_info)
            file.write(line + "\n")

def sair():
    print("Saindo...")
    exit()

def menu(file_path):
    arvore = ArvoreAVL()

    with open(file_path, 'r') as file:
        for line in file:
            animal_info = line.strip().split(',')
            id = animal_info[0]
            apelido = animal_info[1]
            inicio_monitoramento = animal_info[2]
            especie = animal_info[3]
            sexo = animal_info[4]
            data_nascimento = animal_info[5]
            historico_info = animal_info[6:]

            # Cria um objeto Historico com as informações
            data_avaliacao = historico_info[0]
            temperatura = historico_info[1]
            peso = historico_info[2]
            altura = historico_info[3]
            amostra = historico_info[4]
            exame = historico_info[5]
            problema = historico_info[6]
            historico = Historico(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)

            # Cria um objeto Animal com as informações
            animal = Animal(id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico)

            # Insere o objeto Animal na árvore AVL
            arvore.inserir(animal)

    while True:
        arvore.inorder_traversal(arvore.raiz)
        print()
        print("Menu:")
        print("1. Consultar registro")
        print("2. Adicionar registro")
        print("3. Remover registro")
        print("4. Atualizar registro")
        print("5. Salvar alterações")
        print("6. Sair")

        choice = input("Digite sua escolha: ")

        if choice == "1":
            consultar_registro(arvore, input("Digite o ID do animal: "))
        elif choice == "2":
            adicionar_registro(arvore)
        elif choice == "3":
            remover_registro(arvore, input("Digite o ID do animal: "))
        elif choice == "4":
            atualizar_registro(arvore, input("Digite o ID do animal: "))
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
