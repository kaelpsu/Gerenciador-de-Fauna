import manager
import pytest
import sys
import json
from io import StringIO

CAMINHO_PARA_DADOS_DOS_TESTES = "data/test/test_data.json"


@pytest.fixture
def capturar_saida_padrao():
    """
    Fixture para capturar a saída padrão durante os testes.

    Redireciona a saída padrão para um buffer temporário para que possamos verificar
    as mensagens que seriam impressas no terminal durante a execução do teste.

    Retorna:
        StringIO: Um buffer para capturar a saída padrão (sys.stdout).
    """
    output_stream = StringIO("")
    original_output = sys.stdout
    sys.stdout = output_stream
    yield output_stream
    sys.stdout = original_output


def test_inserir_animal(capturar_saida_padrao):
    """
    Teste de inserção de um animal na aplicação.

    Verifica se, ao inserir um novo animal com dados válidos, o sistema retorna
    uma mensagem contendo o nome do animal encontrado. O teste lida com a entrada
    padrão para fornecer os dados necessários para a operação.

    Parâmetros:
        capturar_saida_padrao (StringIO): Buffer onde a saída do sistema será capturada.
    """
    entrada_original = sys.stdin
    entrada = StringIO("1\n5\n6\n6\n")
    sys.stdin = entrada
    with pytest.raises(SystemExit):  # Lida com a saída do programa (exit())
        manager.initialize(CAMINHO_PARA_DADOS_DOS_TESTES)
        assert "Animal encontrado" in capturar_saida_padrao.getvalue()
        sys.stdin = entrada_original


def test_inserir_registro(capturar_saida_padrao):
    """
    Teste de inserção de um registro para um animal na aplicação.

    Verifica se, ao adicionar um registro de monitoramento para um animal, o sistema
    exibe as informações do novo registro inserido corretamente, incluindo os dados fornecidos.

    Parâmetros:
        capturar_saida_padrao (StringIO): Buffer onde a saída do sistema será capturada.
    """
    entrada_original = sys.stdin
    entrada = StringIO("4\n5\ns\n12/12/2025\n36\n13\n121\ns\ns\n1\n5\n6\n6")
    sys.stdin = entrada
    with pytest.raises(SystemExit):  # Lida com a saída do programa (exit())
        manager.initialize(CAMINHO_PARA_DADOS_DOS_TESTES)
        assert (
            "12/12/2004\t\t35\t\t13\t\t121\t\tTrue\t\tTrue\t\tNone"
            in capturar_saida_padrao.getvalue()
        )
        sys.stdin = entrada_original


def test_remover_registro(capturar_saida_padrao):
    """
    Teste de remoção de um registro de monitoramento de um animal.

    Verifica se, ao tentar remover o registro de um animal existente, a mensagem
    esperada de não encontrar o registro na lista de animais é exibida.

    Parâmetros:
        capturar_saida_padrao (StringIO): Buffer onde a saída do sistema será capturada.
    """
    entrada_original = sys.stdin
    entrada = StringIO("3\n5\n6\n6\n")
    sys.stdin = entrada
    with pytest.raises(SystemExit):  # Lida com a saída do programa (exit())
        manager.initialize(CAMINHO_PARA_DADOS_DOS_TESTES)
        assert "ID: 5 | APELIDO: Max" not in capturar_saida_padrao.getvalue()
        sys.stdin = entrada_original


def test_salvar_alteracoes():
    """
    Teste de salvamento das alterações feitas nos dados.

    Verifica se, ao salvar as alterações em um novo arquivo, os dados do novo arquivo
    são iguais aos dados esperados, confirmando que a operação de salvamento funcionou corretamente.

    Parâmetros:
        Nenhum diretamente, pois o teste interage com arquivos e entrada padrão.
    """
    entrada_original = sys.stdin
    novo_caminho = "data/integration_test.json"
    caminho_resultado_esperado = "data/test/salvar_alteracoes_test.json"
    entrada = StringIO(f"3\n5\n5\n{novo_caminho}\n6\n6\n")
    sys.stdin = entrada
    with pytest.raises(SystemExit):  # Lida com a saída do programa (exit())
        manager.initialize(CAMINHO_PARA_DADOS_DOS_TESTES)
        novos_dados = json.load(novo_caminho)
        dados_esperados = json.load(caminho_resultado_esperado)
        assert novos_dados == dados_esperados
        sys.stdin = entrada_original


def test_insercao_existente(capturar_saida_padrao):
    """
    Teste de tentativa de inserção de um animal com ID já existente.

    Verifica se o sistema exibe a mensagem correta quando tenta-se adicionar um animal
    com um ID que já está em uso, evitando a duplicação de IDs.

    Parâmetros:
        capturar_saida_padrao (StringIO): Buffer onde a saída do sistema será capturada.
    """
    entrada_original = sys.stdin
    entrada = StringIO("5\n5\nn\n6\n6\n")
    sys.stdin = entrada
    with pytest.raises(SystemExit):  # Lida com a saída do programa (exit())
        manager.initialize("data/test_data.json")
        assert (
            "Animal com ID já existente. Por favor, escolha outro ID."
            in capturar_saida_padrao.getvalue()
        )
        sys.stdin = entrada_original
