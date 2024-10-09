from animal import Registro
import datetime

def solicita_id():
    id = input("Digite o ID do animal: ")
    while not id.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        id = input("Digite o ID do animal: ")
    return int(id)

def solicita_apelido():
    apelido = input("Digite o apelido do animal: ")
    while not apelido.isalpha():
        print("Valor inválido. Por favor, digite novamente.")
        apelido = input("Digite o apelido do animal: ")
    return apelido

def solicita_data():
    data = input("Digite a data de início do monitoramento do animal (DD/MM/AAAA): ")
    while True:
        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite novamente.")
            data = input("Digite a data de início do monitoramento do animal (DD/MM/AAAA): ")
    return data

def solicita_especie():
    especie = input("Digite a espécie do animal: ")
    while not especie.isalpha():
        print("Valor inválido. Por favor, digite novamente.")
        especie = input("Digite a espécie do animal: ")
    return especie

def solicita_sexo():
    sexo = input("Digite o sexo do animal (M/F): ")
    while sexo not in ["M", "F"]:
        print("Valor inválido. Por favor, digite novamente.")
        sexo = input("Digite o sexo do animal: ")
    return sexo

def solicita_data_nascimento():
    data = input("Digite a data de nascimento do animal (DD/MM/AAAA): ")
    while True:
        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite novamente.")
            data = input("Digite a data de nascimento do animal (DD/MM/AAAA): ")
    return data

def solicita_data_avaliacao():
    data = input("Digite a data da avaliação (DD/MM/AAAA): ")
    while True:
        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite novamente.")
            data = input("Digite a data da avaliação (DD/MM/AAAA): ")
    return data

def solicita_temperatura():
    temperatura = input("Digite a temperatura (C°): ")
    while not temperatura.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        temperatura = input("Digite a temperatura (C°): ")
    return temperatura

def solicita_peso():
    peso = input("Digite o peso (Kg): ")
    while not peso.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        peso = input("Digite o peso (Kg): ")
    return peso

def solicita_altura():
    altura = input("Digite a altura (Cm): ")
    while not altura.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        altura = input("Digite a altura (Cm): ")
    return altura

def solicita_registro():
    data_avaliacao = solicita_data_avaliacao()

    temperatura = solicita_temperatura()

    peso = solicita_peso()
    
    altura = solicita_altura()

    amostra = input("Foi coletada amostra de sangue? (S/N): ")
    exame = input("O exame físico está ok? (S/N): ")

    tem_amostra = amostra.lower() == "s"
    exame_ok = exame.lower() == "s"
    problema = None

    if not exame_ok:
        problema = input("Digite o problema de saúde: ")

    return Registro(data_avaliacao, temperatura, peso, altura, tem_amostra, exame_ok, problema)