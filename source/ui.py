from animal import Registro
import datetime

def solicita_id():
    """
    Solicita e valida o ID do animal.

    O ID deve ser um número inteiro positivo.

    :return: O ID do animal.
    :rtype: int
    """
    
    id = input("Digite o ID do animal: ")
    while not id.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        id = input("Digite o ID do animal: ")
    return int(id)

def solicita_apelido():
    """
    Solicita e valida o apelido do animal.

    O apelido deve conter apenas caracteres alfabéticos.

    :return: O apelido do animal.
    :rtype: str
    """
    
    apelido = input("Digite o apelido do animal: ")
    while not apelido.isalpha():
        print("Valor inválido. Por favor, digite novamente.")
        apelido = input("Digite o apelido do animal: ")
    return apelido

def solicita_data():
    """
    Solicita e valida a data de início do monitoramento do animal.

    A data deve estar no formato DD/MM/AAAA.

    :return: A data de início do monitoramento.
    :rtype: str
    """
    
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
    """
    Solicita e valida a espécie do animal.

    A espécie deve conter apenas caracteres alfabéticos.

    :return: A espécie do animal.
    :rtype: str
    """
    
    especie = input("Digite a espécie do animal: ")
    while not especie.isalpha():
        print("Valor inválido. Por favor, digite novamente.")
        especie = input("Digite a espécie do animal: ")
    return especie

def solicita_sexo():
    """
    Solicita e valida o sexo do animal.

    O sexo deve ser "M" (masculino) ou "F" (feminino).

    :return: O sexo do animal.
    :rtype: str
    """
    
    sexo = input("Digite o sexo do animal (M/F): ")
    while sexo not in ["M", "F"]:
        print("Valor inválido. Por favor, digite novamente.")
        sexo = input("Digite o sexo do animal: ")
    return sexo

def solicita_data_nascimento():
    """
    Solicita e valida a data de nascimento do animal.

    A data deve estar no formato DD/MM/AAAA.

    :return: A data de nascimento do animal.
    :rtype: str
    """
    
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
    """
    Solicita e valida a data da avaliação do animal.

    A data deve estar no formato DD/MM/AAAA.

    :return: A data da avaliação.
    :rtype: str
    """
    
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
    """
    Solicita e valida a temperatura do animal.

    A temperatura deve ser um número positivo.

    :return: A temperatura do animal em graus Celsius.
    :rtype: str
    """
    
    temperatura = input("Digite a temperatura (C°): ")
    while not temperatura.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        temperatura = input("Digite a temperatura (C°): ")
    return temperatura

def solicita_peso():
    """
    Solicita e valida o peso do animal.

    O peso deve ser um número positivo.

    :return: O peso do animal em quilogramas.
    :rtype: str
    """
    
    peso = input("Digite o peso (Kg): ")
    while not peso.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        peso = input("Digite o peso (Kg): ")
    return peso

def solicita_altura():
    """
    Solicita e valida a altura do animal.

    A altura deve ser um número positivo.

    :return: A altura do animal em centímetros.
    :rtype: str
    """
    
    altura = input("Digite a altura (Cm): ")
    while not altura.isdigit():
        print("Valor inválido. Por favor, digite novamente.")
        altura = input("Digite a altura (Cm): ")
    return altura

def solicita_registro():
    """
    Solicita os dados para um novo registro no histórico do animal, como data de avaliação, temperatura, peso, altura, 
    coleta de amostra de sangue, exame físico e, se necessário, informações sobre problemas de saúde.

    :return: Um objeto de registro com os dados coletados.
    :rtype: Registro
    """
    
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