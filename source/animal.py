# Classe que representa um registro no histórico
class Registro:
    def __init__(self, data_avaliacao, temperatura, peso, altura, amostra, exame, problema_saude):
        self.data_avaliacao = data_avaliacao
        self.temperatura = temperatura
        self.peso = peso
        self.altura = altura
        self.amostra = amostra
        self.exame = exame
        self.problema_saude = problema_saude

    # Converte o registro em um dicionário
    def to_dict(self):
        return {
            "data_avaliacao": self.data_avaliacao,
            "temperatura": self.temperatura,
            "peso": self.peso,
            "altura": self.altura,
            "amostra": self.amostra,
            "exame": self.exame,
            "problema_saude": self.problema_saude
        }


# Classe que representa o histórico de registros
class Historico:
    def __init__(self, log_list=None):
        if log_list is None:
            log_list = []
        self.log_list = log_list

    # Adiciona um registro ao histórico
    def addLog(self, log):
        self.log_list.append(log)

    # Retorna as informações do histórico
    def get_info(self):
        return self.log_list

    # Converte o histórico em uma lista de dicionários
    def to_dict(self):
        return [log.to_dict() for log in self.log_list]


# Classe que representa um animal
class Animal:
    def __init__(self, id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico=Historico([])):
        self.id = id
        self.apelido = apelido
        self.inicio_monitoramento = inicio_monitoramento
        self.especie = especie
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.historico = historico

    # Adiciona um registro ao histórico do animal
    def addLog(self, log):
        self.historico.addLog(log)

    # Imprime as informações do animal
    def print_info(self):
        print(f"ID: {self.id}")
        print(f"Apelido: {self.apelido}")
        print(f"Início do Monitoramento: {self.inicio_monitoramento}")
        print(f"Espécie: {self.especie}")
        print(f"Sexo: {self.sexo}")
        print(f"Data de Nascimento: {self.data_nascimento}")

        if self.historico:
            print("Histórico de Registros:")
            print("Data\t\tTemperatura\t\tPeso\t\tAltura\t\tAmostra?\t\tExame OK?\t\tProblema de Saúde")
            for log in self.historico.log_list:
                print(f"{log.data_avaliacao}\t{log.temperatura}\t\t\t{log.peso}\t\t{log.altura}\t\t{log.amostra}\t\t\t{log.exame}\t\t\t{log.problema_saude}")
        else:
            print("Não há histórico disponível.")

    # Converte o animal em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "apelido": self.apelido,
            "inicio_monitoramento": self.inicio_monitoramento,
            "especie": self.especie,
            "sexo": self.sexo,
            "data_nascimento": self.data_nascimento,
            "historico": self.historico.to_dict()
        }