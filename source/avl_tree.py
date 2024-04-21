from animal import Animal, Historico

class Node:
    def __init__(self, animal):
        self.chave = animal.id
        self.animal = animal
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def __iter__(self):
        return self._inorder_iterator(self.raiz)
    
    def _inorder_iterator(self, raiz):
        if raiz:
            yield from self._inorder_iterator(raiz.esquerda)
            yield raiz
            yield from self._inorder_iterator(raiz.direita)

    def inserir(self, animal):
        self.raiz = self._inserir(self.raiz, animal)

    def _inserir(self, raiz, animal):
        chave = animal.id
        if not raiz:
            return Node(animal)
        elif chave < raiz.chave:
            raiz.esquerda = self._inserir(raiz.esquerda, animal)
        else:
            raiz.direita = self._inserir(raiz.direita, animal)

        raiz.altura = 1 + max(self._obter_altura(raiz.esquerda), self._obter_altura(raiz.direita))
        fator_balanceamento = self._obter_fator_balanceamento(raiz)

        if fator_balanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self._rotacionar_direita(raiz)
            else:
                raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)
                return self._rotacionar_direita(raiz)
        elif fator_balanceamento < -1:
            if chave > raiz.direita.chave:
                return self._rotacionar_esquerda(raiz)
            else:
                raiz.direita = self._rotacionar_direita(raiz.direita)
                return self._rotacionar_esquerda(raiz)

        return raiz

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, raiz, chave):
        if not raiz:
            return raiz
        elif chave < raiz.chave:
            raiz.esquerda = self._remover(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self._remover(raiz.direita, chave)
        else:
            if not raiz.esquerda:
                return raiz.direita
            elif not raiz.direita:
                return raiz.esquerda
            else:
                minimo = self._obter_minimo(raiz.direita)
                raiz.chave = minimo.chave
                raiz.animal = minimo.animal
                raiz.direita = self._remover(raiz.direita, minimo.chave)

        raiz.altura = 1 + max(self._obter_altura(raiz.esquerda), self._obter_altura(raiz.direita))
        fator_balanceamento = self._obter_fator_balanceamento(raiz)

        if fator_balanceamento > 1:
            if self._obter_fator_balanceamento(raiz.esquerda) >= 0:
                return self._rotacionar_direita(raiz)
            else:
                raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)
                return self._rotacionar_direita(raiz)
        elif fator_balanceamento < -1:
            if self._obter_fator_balanceamento(raiz.direita) <= 0:
                return self._rotacionar_esquerda(raiz)
            else:
                raiz.direita = self._rotacionar_direita(raiz.direita)
                return self._rotacionar_esquerda(raiz)

        return raiz

    def atualizar(self, chave_antiga, animal_atualizado):
        self.remover(chave_antiga)
        self.inserir(animal_atualizado)

    def consultar(self, chave):
        return self._consultar(self.raiz, chave)

    def _consultar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz
        elif chave < raiz.chave:
            return self._consultar(raiz.esquerda, chave)
        else:
            return self._consultar(raiz.direita, chave)

    def _obter_altura(self, node):
        if not node:
            return 0
        return node.altura

    def _obter_fator_balanceamento(self, node):
        if not node:
            return 0
        return self._obter_altura(node.esquerda) - self._obter_altura(node.direita)

    def _rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _obter_minimo(self, raiz):
        atual = raiz
        while atual.esquerda:
            atual = atual.esquerda
        return atual
    
    def inorder_traversal(self, raiz):
        if raiz:
            self.inorder_traversal(raiz.esquerda)
            print(f"ID: {raiz.animal.id} | APELIDO: {raiz.animal.apelido}")
            self.inorder_traversal(raiz.direita)

# Testar a implementação da árvore AVL
if __name__ == "__main__":
    # Create an instance of ArvoreAVL
    arvore = ArvoreAVL()

    # Create some instances of Animal
    # Create instances of Animal
    animal1 = Animal(1, "Lion", "2022-01-01", "Mammal", "Male", "2020-05-10", Historico("2022-01-01", 37.5, 150, 100, "Blood", "X-ray", "None"))
    animal2 = Animal(2, "Tiger", "2022-02-15", "Mammal", "Female", "2021-03-20", Historico("2022-02-15", 38.2, 180, 110, "Urine", "Ultrasound", "None"))
    animal3 = Animal(3, "Elephant", "2022-03-10", "Mammal", "Male", "2020-07-15", Historico("2022-03-10", 36.8, 5000, 300, "Hair", "MRI", "None"))
    animal4 = Animal(4, "Giraffe", "2022-04-20", "Mammal", "Female", "2021-01-05", Historico("2022-04-20", 37.1, 1800, 550, "Saliva", "CT Scan", "None"))
    animal5 = Animal(5, "Penguin", "2022-05-30", "Bird", "Male", "2020-11-25", Historico("2022-05-30", 36.5, 10, 40, "Feathers", "X-ray", "None"))
    animal6 = Animal(6, "Dolphin", "2022-06-10", "Mammal", "Female", "2021-07-12", Historico("2022-06-10", 37.3, 300, 200, "Blubber", "Ultrasound", "None"))
    animal7 = Animal(7, "Kangaroo", "2022-07-20", "Mammal", "Male", "2021-09-05", Historico("2022-07-20", 37.0, 100, 150, "Fur", "MRI", "None"))

    # Insert nodes into the AVL tree
    arvore.inserir(animal1)
    arvore.inserir(animal2)
    arvore.inserir(animal3)
    arvore.inserir(animal4)
    arvore.inserir(animal5)

    # Print the inorder traversal of the AVL tree
    arvore.inorder_traversal(arvore.raiz)

    # Search for a node in the AVL tree
    #node = arvore.consultar(3)
    #node.animal.print_info()

    # Update a node in the AVL tree
    #arvore.atualizar(chave_antiga, animal_atualizado)

    # Remove a node from the AVL tree
    #arvore.remover(2)

    # Print the inorder traversal of the AVL tree
    #arvore.inorder_traversal(arvore.raiz)

    # Print the updated inorder traversal of the AVL tree
    #arvore.inorder_traversal(arvore.raiz)