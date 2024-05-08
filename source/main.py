from avl_tree import ArvoreAVL
from animal import Animal, Historico, Registro
import sys
import json
import datetime

def consultar_animal(arvore, chave):
    node = arvore.consultar(chave)
    if node:
        print("")
        print("Animal encontrado:")
        node.animal.print_info()
    input("Pressione Enter para continuar...")  

def adicionar_animal(arvore):
    # Solicita o ID do animal
    id = int(input("Digite o ID do animal: "))
    # Verifica se o ID já existe na árvore
    while arvore.consultar(id):
        print("")
        print("Animal com ID já existe. Por favor, escolha outro ID.")
        id = input("Digite o ID do animal: ")

    # Solicita o apelido do animal
    apelido = input("Digite o apelido do animal: ")

    # Solicita a data de início do monitoramento do animal e verifica validade do formato
    while True:
        inicio_monitoramento = input("Digite a data de início do monitoramento do animal (DD/MM/AAAA): ")
        try:
            datetime.datetime.strptime(inicio_monitoramento, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite novamente.")

    # Solicita a espécie do animal
    especie = input("Digite a espécie do animal: ")

    # Solicita o sexo do animal
    sexo = input("Digite o sexo do animal (M/F): ")
    # Verifica se o sexo é válido
    while sexo not in ["M", "F"]:
        print("Valor inválido. Por favor, digite novamente.")
        sexo = input("Digite o sexo do animal: ")

    # Solicita a data de nascimento do animal e verifica validade do formato
    while True:
        data_nascimento = input("Digite a data de nascimento do animal: (DD/MM/AAAA): ")
        try:
            datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite novamente.")

    print("")
    # Pergunta se deseja adicionar um registro no histórico
    add_history = input("Deseja adicionar um registro no histórico? (S/N): ")
    if add_history.lower() == "s":
        while True:
            # Solicita a data da avaliação e verifica se está no formato correto
            data_avaliacao = input("Digite a data da avaliação (DD/MM/AAAA): ")
            try:
                datetime.datetime.strptime(data_avaliacao, "%d/%m/%Y")
                break
            except ValueError:
                print("Formato de data inválido. Por favor, digite novamente.")

        while True:
            # Solicita a temperatura e verifica se é um valor válido
            temperatura = input("Digite a temperatura (C°): ")
            if temperatura.isdigit():
                break
            else:
                print("Valor inválido. Por favor, digite novamente.")

        while True:
            # Solicita o peso e verifica se é um valor válido
            peso = input("Digite o peso (Kg): ")
            if peso.isdigit():
                break
            else:
                print("Valor inválido. Por favor, digite novamente.")

        while True:
            # Solicita a altura e verifica se é um valor válido
            altura = input("Digite a altura (Cm): ")
            if altura.isdigit():
                break
            else:
                print("Valor inválido. Por favor, digite novamente.")

        # Pergunta se foi coletada amostra de sangue e se o exame físico está ok
        amostra = input("Foi coletada amostra de sangue (S/N): ")
        exame = input("O exame físico está ok? (S/N): ")
        amostra = amostra.lower() == "s"
        exame = exame.lower() == "s"
        problema = None

        if not exame:
            # Se o exame não estiver ok, solicita o problema de saúde
            problema = input("Digite o problema de saúde: ")

        # Cria um objeto Registro com as informações fornecidas
        registro = Registro(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
        # Cria um objeto Historico com o registro
        historico = Historico([registro])
    else:
        # Cria um objeto Historico vazio
        historico = Historico([])

    # Cria um objeto Animal com as informações fornecidas
    animal = Animal(id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico)

    # Insere o objeto Animal na árvore AVL
    arvore.inserir(animal)

def remover_animal(arvore, chave):
    arvore.remover(chave)

def adicionar_registro(arvore, chave):
    # Consulta o nó correspondente à chave na árvore
    node = arvore.consultar(chave)
    if node:
        print("")
        print("Animal encontrado. Informações atuais:")
        node.animal.print_info()

        print("")
        # Pergunta ao usuário se deseja atualizar o histórico
        historico = input("Deseja atualizar o histórico? (S/N): ")
        if historico.lower() == "s":
            while True:
                # Solicita a data da avaliação e verifica se está no formato correto
                data_avaliacao = input("Digite a data da avaliação (DD/MM/AAAA): ")
                try:
                    datetime.datetime.strptime(data_avaliacao, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Formato de data inválido. Por favor, digite novamente.")

            while True:
                # Solicita a temperatura e verifica se é um valor válido
                temperatura = input("Digite a temperatura (C°): ")
                if temperatura.isdigit():
                    break
                else:
                    print("Valor inválido. Por favor, digite novamente.")

            while True:
                # Solicita o peso e verifica se é um valor válido
                peso = input("Digite o peso (Kg): ")
                if peso.isdigit():
                    break
                else:
                    print("Valor inválido. Por favor, digite novamente.")

            while True:
                # Solicita a altura e verifica se é um valor válido
                altura = input("Digite a altura (Cm): ")
                if altura.isdigit():
                    break
                else:
                    print("Valor inválido. Por favor, digite novamente.")

            # Pergunta se foi coletada amostra de sangue e se o exame físico está ok
            amostra = input("Foi coletada amostra de sangue (S/N): ")
            exame = input("O exame físico está ok? (S/N): ")
            amostra = amostra.lower() == "s"
            exame = exame.lower() == "s"
            problema = None

            if not exame:
                # Se o exame não estiver ok, solicita o problema de saúde
                problema = input("Digite o problema de saúde: ")

            # Cria um objeto Registro com as informações fornecidas
            registro = Registro(data_avaliacao, temperatura, peso, altura, amostra, exame, problema)
            # Adiciona o registro ao histórico do animal
            node.animal.addLog(registro)

# Função para salvar as alterações no arquivo
def salvar_alteracoes(arvore, save_path):
    with open(save_path, 'w') as file:
        animals = []

        # Percorre todos os nós da árvore e adiciona os animais na lista
        for node in arvore:
            animals.append(node.animal)

        # Cria um dicionário com a lista de animais e escreve no arquivo JSON
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
            # animal.print_info()

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
            save_path = input("Digite o caminho do arquivo para salvar as alterações: ")
            salvar_alteracoes(arvore, save_path)
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
