from animal import Animal, Historico

class Node:
    def __init__(self, animal):
        self.chave = animal.id  # Chave do nó é o ID do animal
        self.animal = animal  # Referência para o objeto Animal
        self.esquerda = None  # Referência para o nó filho esquerdo
        self.direita = None  # Referência para o nó filho direito
        self.altura = 1  # Altura do nó na árvore

class ArvoreAVL:
    def __init__(self):
        self.raiz = None  # Referência para o nó raiz da árvore

    def __iter__(self):
        return self._inorder_iterator(self.raiz)

    def _inorder_iterator(self, raiz):
        if raiz:
            yield from self._inorder_iterator(raiz.esquerda)  # Percorre a subárvore esquerda
            yield raiz  # Retorna o nó atual
            yield from self._inorder_iterator(raiz.direita)  # Percorre a subárvore direita

    def inserir(self, animal):
        self.raiz = self._inserir(self.raiz, animal)

    def _inserir(self, raiz, animal):
        chave = animal.id
        if not raiz:
            return Node(animal)  # Cria um novo nó se a raiz for nula
        elif chave < raiz.chave:
            raiz.esquerda = self._inserir(raiz.esquerda, animal)  # Insere na subárvore esquerda
        else:
            raiz.direita = self._inserir(raiz.direita, animal)  # Insere na subárvore direita

        raiz.altura = 1 + max(self._obter_altura(raiz.esquerda), self._obter_altura(raiz.direita))  # Atualiza a altura do nó
        fator_balanceamento = self._obter_fator_balanceamento(raiz)  # Calcula o fator de balanceamento do nó

        if fator_balanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self._rotacionar_direita(raiz)  # Rotação simples à direita
            else:
                raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)  # Rotação dupla à esquerda
                return self._rotacionar_direita(raiz)  # Rotação simples à direita
        elif fator_balanceamento < -1:
            if chave > raiz.direita.chave:
                return self._rotacionar_esquerda(raiz)  # Rotação simples à esquerda
            else:
                raiz.direita = self._rotacionar_direita(raiz.direita)  # Rotação dupla à direita
                return self._rotacionar_esquerda(raiz)  # Rotação simples à esquerda

        return raiz

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, raiz, chave):
        if not raiz:
            return raiz
        elif chave < raiz.chave:
            raiz.esquerda = self._remover(raiz.esquerda, chave)  # Remove da subárvore esquerda
        elif chave > raiz.chave:
            raiz.direita = self._remover(raiz.direita, chave)  # Remove da subárvore direita
        else:
            if not raiz.esquerda:
                return raiz.direita  # Substitui o nó pelo filho direito
            elif not raiz.direita:
                return raiz.esquerda  # Substitui o nó pelo filho esquerdo
            else:
                minimo = self._obter_minimo(raiz.direita)  # Encontra o nó mínimo na subárvore direita
                raiz.chave = minimo.chave  # Substitui a chave do nó pelo mínimo encontrado
                raiz.animal = minimo.animal  # Substitui o objeto Animal do nó pelo mínimo encontrado
                raiz.direita = self._remover(raiz.direita, minimo.chave)  # Remove o mínimo encontrado da subárvore direita

        raiz.altura = 1 + max(self._obter_altura(raiz.esquerda), self._obter_altura(raiz.direita))  # Atualiza a altura do nó
        fator_balanceamento = self._obter_fator_balanceamento(raiz)  # Calcula o fator de balanceamento do nó

        if fator_balanceamento > 1:
            if self._obter_fator_balanceamento(raiz.esquerda) >= 0:
                return self._rotacionar_direita(raiz)  # Rotação simples à direita
            else:
                raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)  # Rotação dupla à esquerda
                return self._rotacionar_direita(raiz)  # Rotação simples à direita
        elif fator_balanceamento < -1:
            if self._obter_fator_balanceamento(raiz.direita) <= 0:
                return self._rotacionar_esquerda(raiz)  # Rotação simples à esquerda
            else:
                raiz.direita = self._rotacionar_direita(raiz.direita)  # Rotação dupla à direita
                return self._rotacionar_esquerda(raiz)  # Rotação simples à esquerda

        return raiz

    def atualizar(self, chave_antiga, animal_atualizado):
        self.remover(chave_antiga)  # Remove o nó com a chave antiga
        self.inserir(animal_atualizado)  # Insere o nó atualizado

    def consultar(self, chave):
        return self._consultar(self.raiz, chave)

    def _consultar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz  # Retorna o nó se a chave for encontrada ou se a raiz for nula
        elif chave < raiz.chave:
            return self._consultar(raiz.esquerda, chave)  # Procura na subárvore esquerda
        else:
            return self._consultar(raiz.direita, chave)  # Procura na subárvore direita

    def _obter_altura(self, node):
        if not node:
            return 0
        return node.altura  # Retorna a altura do nó

    def _obter_fator_balanceamento(self, node):
        if not node:
            return 0
        return self._obter_altura(node.esquerda) - self._obter_altura(node.direita)  # Calcula o fator de balanceamento do nó

    def _rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))  # Atualiza a altura do nó z
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))  # Atualiza a altura do nó y

        return y

    def _rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))  # Atualiza a altura do nó z
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))  # Atualiza a altura do nó y

        return y

    def _obter_minimo(self, raiz):
        atual = raiz
        while atual.esquerda:
            atual = atual.esquerda
        return atual  # Retorna o nó mínimo encontrado

    def inorder_traversal(self, raiz):
        if raiz:
            self.inorder_traversal(raiz.esquerda)  # Percorre a subárvore esquerda
            print(f"ID: {raiz.animal.id} | APELIDO: {raiz.animal.apelido}")  # Imprime as informações do nó
            self.inorder_traversal(raiz.direita)  # Percorre a subárvore direita
