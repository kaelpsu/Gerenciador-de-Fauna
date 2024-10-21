class Registro:
    """
    Representa um registro de avaliação de um animal.

    :param data_avaliacao: Data da avaliação.
    :type data_avaliacao: str
    :param temperatura: Temperatura medida durante a avaliação.
    :type temperatura: float
    :param peso: Peso do animal.
    :type peso: float
    :param altura: Altura do animal.
    :type altura: float
    :param amostra: Indicador se foi coletada uma amostra.
    :type amostra: bool
    :param exame: Indicador se o exame foi aprovado.
    :type exame: bool
    :param problema_de_saude: Descrição do problema de saúde (se houver).
    :type problema_de_saude: str
    """
    
    def __init__(self, data_avaliacao, temperatura, peso, altura, amostra, exame, problema_de_saude):
        self.data_avaliacao = data_avaliacao
        self.temperatura = temperatura
        self.peso = peso
        self.altura = altura
        self.amostra = amostra
        self.exame = exame
        self.problema_de_saude = problema_de_saude

    def convert_to_dictionary(self):
        """
        Converte o registro em um dicionário.

        :return: Dicionário com os dados do registro.
        :rtype: dict
        """
        
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
    """
    Representa o histórico de avaliações de um animal.

    :param logs: Lista de registros de avaliação. Por padrão, inicia como uma lista vazia.
    :type logs: list
    """
    
    def __init__(self, logs=None):
        if logs is None:
            logs = []
        self.logs = logs

    def add_log(self, log):
        """
        Adiciona um novo registro ao histórico.

        :param log: Registro a ser adicionado.
        :type log: Registro
        """
        
        self.logs.append(log)

    def get_info(self):
        """
        Retorna a lista de registros no histórico.

        :return: Lista de registros.
        :rtype: list
        """
        
        return self.logs

    def convert_to_dictionary(self):
        """
        Converte o histórico em uma lista de dicionários.

        :return: Lista de dicionários com os dados dos registros.
        :rtype: list
        """
        
        return [log.convert_to_dictionary() for log in self.logs]


class Animal:
    """
    Representa um animal e seu histórico de avaliações.

    :param id: Identificação do animal.
    :type id: int
    :param apelido: Apelido do animal.
    :type apelido: str
    :param inicio_monitoramento: Data de início do monitoramento.
    :type inicio_monitoramento: str
    :param especie: Espécie do animal.
    :type especie: str
    :param sexo: Sexo do animal.
    :type sexo: str
    :param data_nascimento: Data de nascimento do animal.
    :type data_nascimento: str
    :param historico: Histórico de avaliações do animal.
    :type historico: Historico
    """
    
    def __init__(self, id, apelido, inicio_monitoramento, especie, sexo, data_nascimento, historico=Historico([])):
        self.id = id
        self.apelido = apelido
        self.inicio_monitoramento = inicio_monitoramento
        self.especie = especie
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.historico = historico

    def add_log(self, log):
        """
        Adiciona um novo registro de avaliação ao histórico do animal.

        :param log: Registro a ser adicionado.
        :type log: Registro
        """
        
        self.historico.add_log(log)
        
    def print_historico(self):
        """
        Exibe o histórico de avaliações do animal em formato de tabela.
        """
        
        print("Histórico de Registros:")
        print("Data\t\tTemperatura\t\tPeso\t\tAltura\t\tAmostra?\t\tExame OK?\t\tProblema de Saúde")

        for log in self.historico.logs:
            print(f"{log.data_avaliacao}\t{log.temperatura}\t\t\t{log.peso}\t\t{log.altura}\t\t{log.amostra}\t\t\t{log.exame}\t\t\t{log.problema_de_saude}")

    def print_info(self):
        """
        Exibe as informações do animal e seu histórico (se houver).
        """
        
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
        """
        Converte os dados do animal e seu histórico em um dicionário.

        :return: Dicionário com os dados do animal e seu histórico.
        :rtype: dict
        """
        
        return {
            "id": self.id,
            "apelido": self.apelido,
            "inicio_monitoramento": self.inicio_monitoramento,
            "especie": self.especie,
            "sexo": self.sexo,
            "data_nascimento": self.data_nascimento,
            "historico": self.historico.convert_to_dictionary(),
        }
