# Estrutura de dados utilizada para armazenar os registros da aplicação

class Node:
    def __init__(self, animal):
        self.chave = animal.id
        self.animal = animal
        self.filho_esquerdo = None
        self.filho_direito = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def __iter__(self):
        return self._inorder_iterator(self.raiz)

    def _inorder_iterator(self, raiz):
        if raiz:
            yield from self._inorder_iterator(raiz.filho_esquerdo)  # Percorre a subárvore esquerda
            yield raiz  # Retorna o nó atual
            yield from self._inorder_iterator(raiz.filho_direito)  # Percorre a subárvore direita

    def inserir(self, animal):
        self.raiz = self._inserir(self.raiz, animal)

    def _inserir(self, raiz, animal):
        chave = animal.id
        if not raiz:
            return Node(animal)
        elif chave < raiz.chave:
            raiz.filho_esquerdo = self._inserir(raiz.filho_esquerdo, animal)  # Insere na subárvore esquerda
        else:
            raiz.filho_direito = self._inserir(raiz.filho_direito, animal)  # Insere na subárvore direita

        self._atualizar_altura(raiz)
        fator_balanceamento = self._obter_fator_balanceamento(raiz)

        if fator_balanceamento > 1:
            if chave < raiz.filho_esquerdo.chave:
                return self._rotacionar_direita(raiz) 
            else:
                raiz.filho_esquerdo = self._rotacionar_esquerda(raiz.filho_esquerdo)  # Rotação dupla à esquerda
                return self._rotacionar_direita(raiz)
        elif fator_balanceamento < -1:
            if chave > raiz.filho_direito.chave:
                return self._rotacionar_esquerda(raiz)
            else:
                raiz.filho_direito = self._rotacionar_direita(raiz.filho_direito)  # Rotação dupla à direita
                return self._rotacionar_esquerda(raiz)

        return raiz

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, raiz, chave):
        if not raiz:
            return raiz
        elif chave < raiz.chave:
            raiz.filho_esquerdo = self._remover(raiz.filho_esquerdo, chave)  # Remove da subárvore esquerda
        elif chave > raiz.chave:
            raiz.filho_direito = self._remover(raiz.filho_direito, chave)  # Remove da subárvore direita
        else:
            if not raiz.filho_esquerdo:
                return raiz.filho_direito  # Substitui o nó pelo filho direito
            elif not raiz.filho_direito:
                return raiz.filho_esquerdo  # Substitui o nó pelo filho esquerdo
            else:
                minimo = self._obter_nó_minimo(raiz.filho_direito)
                raiz.chave = minimo.chave
                raiz.animal = minimo.animal
                raiz.filho_direito = self._remover(raiz.filho_direito, minimo.chave)

        self._atualizar_altura(raiz)
        fator_balanceamento = self._obter_fator_balanceamento(raiz)

        if fator_balanceamento > 1:
            if self._obter_fator_balanceamento(raiz.filho_esquerdo) >= 0:
                return self._rotacionar_direita(raiz)
            else:
                raiz.filho_esquerdo = self._rotacionar_esquerda(raiz.filho_esquerdo)  # Rotação dupla à esquerda
                return self._rotacionar_direita(raiz)
        elif fator_balanceamento < -1:
            if self._obter_fator_balanceamento(raiz.filho_direito) <= 0:
                return self._rotacionar_esquerda(raiz)
            else:
                raiz.filho_direito = self._rotacionar_direita(raiz.filho_direito)  # Rotação dupla à direita
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
            return self._consultar(raiz.filho_esquerdo, chave)  # Procura na subárvore esquerda
        else:
            return self._consultar(raiz.filho_direito, chave)  # Procura na subárvore direita

    def _obter_altura(self, node):
        if not node:
            return 0
        return node.altura
    
    def _atualizar_altura(self, node):
        if not node:
            return 0
        node.altura = 1 + max(self._obter_altura(node.filho_esquerdo), self._obter_altura(node.filho_direito))

    def _obter_fator_balanceamento(self, node):
        if not node:
            return 0
        return self._obter_altura(node.filho_esquerdo) - self._obter_altura(node.filho_direito)  # Calcula o fator de balanceamento do nó

    def _rotacionar_esquerda(self, node):
        filho_direito = node.filho_direito
        neto = filho_direito.filho_esquerdo

        filho_direito.filho_esquerdo = node
        node.filho_direito = neto

        self._atualizar_altura(node)
        self._atualizar_altura(filho_direito)

        return filho_direito

    def _rotacionar_direita(self, node):
        filho_esquerdo = node.filho_esquerdo
        neto = filho_esquerdo.filho_direito

        filho_esquerdo.filho_direito = node
        node.filho_esquerdo = neto

        self._atualizar_altura(node)
        self._atualizar_altura(filho_esquerdo)

        return filho_esquerdo

    def _obter_nó_minimo(self, raiz):
        minimo = raiz
        while minimo.filho_esquerdo:
            minimo = minimo.filho_esquerdo
        return minimo

    def inorder_traversal(self, raiz):
        if raiz:
            self.inorder_traversal(raiz.filho_esquerdo)  # Percorre a subárvore esquerda
            print(f"ID: {raiz.animal.id} | APELIDO: {raiz.animal.apelido}")  # Imprime as informações do nó
            self.inorder_traversal(raiz.filho_direito)  # Percorre a subárvore direita
