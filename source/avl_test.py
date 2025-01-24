import pytest
from animal import Animal
from unittest.mock import Mock


@pytest.fixture
def arvore_vazia():
    """
    Fixture para criar uma instância de uma árvore AVL vazia.

    Retorna:
        ArvoreAVL: Uma árvore AVL vazia para ser usada em testes.
    """
    from avl_tree import ArvoreAVL

    return ArvoreAVL()


@pytest.fixture
def animal_mocks():
    """
    Fixture para criar uma lista de mocks de animais, com IDs e apelidos definidos.

    Retorna:
        list: Uma lista de 10 mocks de objetos `Animal`, com apelidos e IDs configurados.
    """
    mocks = [Mock(spec=Animal) for i in range(0, 10)]
    names = [
        "Alfa",
        "Bravo",
        "Charlie",
        "Delta",
        "Echo",
        "Foxtrot",
        "Golf",
        "Hotel",
        "India",
        "Juliett",
    ]
    id = 0
    for mock in mocks:
        mock.id = id
        mock.apelido = names[id]
        id += 1
    return mocks


@pytest.fixture
def arvore_cheia(animal_mocks):
    """
    Fixture para criar uma árvore AVL cheia com 10 animais mockados.

    Parâmetros:
        animal_mocks (list): Lista de mocks de animais para inserir na árvore.

    Retorna:
        ArvoreAVL: Uma árvore AVL contendo os animais mockados.
    """
    from avl_tree import ArvoreAVL

    arvore = ArvoreAVL()
    for animal_mock in animal_mocks:
        arvore.inserir(animal_mock)
    return arvore


def test_consulta(arvore_cheia):
    """
    Teste de consulta de um animal na árvore AVL.

    Verifica se a consulta de um animal com ID válido retorna um resultado esperado.

    Parâmetros:
        arvore_cheia (ArvoreAVL): A árvore cheia com animais.
    """
    assert arvore_cheia.consultar(1)


def test_insercao(arvore_vazia):
    """
    Teste de inserção de um animal na árvore AVL.

    Verifica se a inserção de um novo animal na árvore está funcionando corretamente.

    Parâmetros:
        arvore_vazia (ArvoreAVL): A árvore vazia onde o animal será inserido.
    """
    animal = Animal(1, "Jackie", "01/01/2025", "Raccoon", "F", "22/03/2023")
    arvore_vazia.inserir(animal)
    assert arvore_vazia.consultar(animal.id).animal.__eq__(animal)


def test_remocao(arvore_cheia):
    """
    Teste de remoção de um animal na árvore AVL.

    Verifica se a remoção de um animal com ID válido está funcionando corretamente.

    Parâmetros:
        arvore_cheia (ArvoreAVL): A árvore cheia onde o animal será removido.
    """
    arvore_cheia.remover(1)
    assert not arvore_cheia.consultar(1)


def test_remocao_animal_inexistente(arvore_cheia):
    """
    Teste de remoção de um animal inexistente na árvore AVL.

    Verifica se a remoção de um animal que não existe retorna o valor esperado (False).

    Parâmetros:
        arvore_cheia (ArvoreAVL): A árvore cheia onde a tentativa de remoção será realizada.
    """
    assert not arvore_cheia.remover(20)


def test_atualizar(arvore_cheia):
    """
    Teste de atualização de um animal existente na árvore AVL.

    Verifica se a atualização de um animal com ID existente está funcionando corretamente.

    Parâmetros:
        arvore_cheia (ArvoreAVL): A árvore cheia onde o animal será atualizado.
    """
    novo_animal = Mock(spec=Animal)
    novo_animal.id = 11
    novo_animal.apelido = str(11)
    arvore_cheia.atualizar(10, novo_animal)
    assert arvore_cheia.consultar(novo_animal.id)


def test_atualizar_inexistente(arvore_cheia):
    """
    Teste de atualização de um animal inexistente na árvore AVL.

    Verifica se ao tentar atualizar um animal que não existe, um novo registro é criado.

    Parâmetros:
        arvore_cheia (ArvoreAVL): A árvore cheia onde a tentativa de atualização será realizada.
    """
    novo_animal = Mock(spec=Animal)
    novo_animal.id = 14
    novo_animal.apelido = "Nova"
    arvore_cheia.atualizar(14, novo_animal)
    # Testa se, ao atualizar um elemento inexistente, um novo registro é criado
    assert arvore_cheia.consultar(14)
