import time
from avl_tree import ArvoreAVL
from animal import Animal
import random

# Função para medir o tempo de execução de busca
def measure_time(search_function, *args):
    start_time = time.time_ns()
    result = search_function(*args)
    end_time = time.time_ns()
    return result, end_time - start_time

# Busca linear na lista de animais
def linear_search(array, key):
    for animal in array:
        if animal.id == key:
            return animal
    return None

# Busca em árvore AVL
def avl_search(tree, key):
    return tree.consultar(key)  # AVLTree.search retorna True se o elemento está na árvore

# Mock de geração de animais
def generate_animals(size):
    animals = []
    for i in range(size):
        animal = Animal(
            id=i,
            apelido=f"Animal_{i}",
            inicio_monitoramento="2025-01-01",
            especie="Espécie X",
            sexo=random.choice(["M", "F"]),
            data_nascimento="2020-01-01",
        )
        animals.append(animal)
    return animals


# Inicializando o benchmark
def benchmark():
    sizes = [50, 5000, 100000, 1000000]  # Tamanhos diferentes de dados para o benchmark
    search_key = 999999  # ID do animal a ser procurado

    for size in sizes:
        print(f"\n### Testando com {size} elementos ###")

        # Gerando os animais
        animals = generate_animals(size)

        # Criando e preenchendo a árvore AVL
        avl_tree = ArvoreAVL()
        for animal in animals:
            avl_tree.inserir(animal)  # ID como chave, objeto Animal como valor

        # Teste na lista
        _, linear_time = measure_time(linear_search, animals, search_key)
        print(f"Tempo de busca linear (lista): {linear_time} ns")

        # Teste na árvore AVL
        _, avl_time = measure_time(avl_search, avl_tree, search_key)
        print(f"Tempo de busca (AVL): {avl_time} ns")



benchmark()
