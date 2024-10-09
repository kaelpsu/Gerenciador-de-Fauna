class Registro:
    def __init__(self, data_avaliacao, temperatura, peso, altura, amostra, exame, problema_de_saude):
        self.data_avaliacao = data_avaliacao
        self.temperatura = temperatura
        self.peso = peso
        self.altura = altura
        self.amostra = amostra
        self.exame = exame
        self.problema_de_saude = problema_de_saude

    def convert_to_dictionary(self):
        return {
            "data_avaliacao": self.data_avaliacao,
            "temperatura": self.temperatura,
            "peso": self.peso,
            "altura": self.altura,
            "amostra": self.amostra,
            "exame": self.exame,
            "problema_de_saude": self.problema_de_saude
        }


class Historico:
    def __init__(self, logs=None):
        if logs is None:
            logs = []
        self.logs = logs

    def add_log(self, log):
        self.logs.append(log)

    def get_info(self):
        return self.logs

    def convert_to_dictionary(self):
        return [log.convert_to_dictionary() for log in self.logs]


class Animal:
    def __init__(self, id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico=Historico([])):
        self.id = id
        self.apelido = apelido
        self.inicio_monitoramento = inicio_monitoramento
        self.especie = especie
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.historico = historico

    def add_log(self, log):
        self.historico.add_log(log)
        
    def print_historico(self):
        print("Histórico de Registros:")
        print("Data\t\tTemperatura\t\tPeso\t\tAltura\t\tAmostra?\t\tExame OK?\t\tProblema de Saúde")

        for log in self.historico.logs:
            print(f"{log.data_avaliacao}\t{log.temperatura}\t\t\t{log.peso}\t\t{log.altura}\t\t{log.amostra}\t\t\t{log.exame}\t\t\t{log.problema_de_saude}")

    def print_info(self):
        print(f"ID: {self.id}")
        print(f"Apelido: {self.apelido}")
        print(f"Início do Monitoramento: {self.inicio_monitoramento}")
        print(f"Espécie: {self.especie}")
        print(f"Sexo: {self.sexo}")
        print(f"Data de Nascimento: {self.data_nascimento}")

        if self.historico:
            self.print_historico()
        else:
            print("Não há histórico disponível.")

    def convert_to_dictionary(self):
        return {
            "id": self.id,
            "apelido": self.apelido,
            "inicio_monitoramento": self.inicio_monitoramento,
            "especie": self.especie,
            "sexo": self.sexo,
            "data_nascimento": self.data_nascimento,
            "historico": self.historico.convert_to_dictionary(),
        }
