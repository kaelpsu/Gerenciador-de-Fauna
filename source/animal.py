class Animal:
    def __init__(self, id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico=None):
        self.id = id
        self.apelido = apelido
        self.inicio_monitoramento = inicio_monitoramento
        self.especie = especie
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.historico = historico

    def print_info(self):
        print(f"ID: {self.id}")
        print(f"Apelido: {self.apelido}")
        print(f"Início do Monitoramento: {self.inicio_monitoramento}")
        print(f"Espécie: {self.especie}")
        print(f"Sexo: {self.sexo}")
        print(f"Data de Nascimento: {self.data_nascimento}")

        if self.historico:
            print("Histórico:")
            print(f"    Data da Avaliação: {self.historico.data_avaliacao}")
            print(f"    Temperatura: {self.historico.temperatura}")
            print(f"    Peso: {self.historico.peso}")
            print(f"    Altura: {self.historico.altura}")
            print(f"    Amostra de Sangue?: {self.historico.amostra}")
            print(f"    Exame Ok?: {self.historico.exame}")
            print(f"    Problema de Saúde: {self.historico.problema_saude}")

class Historico:
    def __init__(self, data_avaliacao, temperatura, peso, altura, amostra, exame, problema_saude):
        self.data_avaliacao = data_avaliacao
        self.temperatura = temperatura
        self.peso = peso
        self.altura = altura
        self.amostra = amostra
        self.exame = exame
        self.problema_saude = problema_saude

    def get_info(self):
        return [self.data_avaliacao, self.temperatura, self.peso, self.altura, self.amostra, self.exame, self.problema_saude]

