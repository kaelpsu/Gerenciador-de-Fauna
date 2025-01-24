from io import StringIO
# Estrutura de dados utilizada para armazenar os registros da aplicação

class Node:
    """
    Representa um nó de uma árvore AVL.

    :param animal: Objeto da classe `Animal` que será armazenado no nó.
    :type animal: Animal
    """

    def __init__(self, animal):
        self.chave = animal.id
        self.animal = animal
        self.filho_esquerdo = None
        self.filho_direito = None
        self.altura = 1

class ArvoreAVL:
    """
    Implementa uma árvore AVL para armazenar e gerenciar objetos `Animal`.

    A árvore AVL é uma árvore de busca binária balanceada, que garante que as operações de inserção,
    remoção e consulta sejam feitas em tempo O(log n).
    """

    def __init__(self):
        """
        Inicializa a árvore AVL vazia.
        """

        self.raiz = None

    def __iter__(self):
        """
        Retorna um iterador que percorre a árvore em ordem.

        :return: Iterador que percorre a árvore.
        :rtype: iter
        """

        return self._inorder_iterator(self.raiz)

    def _inorder_iterator(self, raiz):
        """
        Iterador interno para percorrer a árvore em ordem.

        :param raiz: Raiz da subárvore a ser percorrida.
        :type raiz: Node
        :return: Um gerador para os nós da árvore em ordem.
        :rtype: generator
        """

        if raiz:
            yield from self._inorder_iterator(raiz.filho_esquerdo)  # Percorre a subárvore esquerda
            yield raiz  # Retorna o nó atual
            yield from self._inorder_iterator(raiz.filho_direito)  # Percorre a subárvore direita

    def inserir(self, animal):
        """
        Insere um novo animal na árvore AVL.

        :param animal: O animal a ser inserido.
        :type animal: Animal
        """

        self.raiz = self._inserir(self.raiz, animal)

    def _inserir(self, raiz, animal):
        """
        Função recursiva para inserir um novo nó na árvore AVL.

        :param raiz: Raiz da subárvore onde o novo nó será inserido.
        :type raiz: Node
        :param animal: O animal a ser inserido.
        :type animal: Animal
        :return: O nó raiz atualizado após a inserção e balanceamento.
        :rtype: Node
        """

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
        """
        Remove um nó da árvore AVL com base na chave do animal.

        :param chave: A chave (ID do animal) a ser removida.
        :type chave: int
        """

        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, raiz, chave):
        """
        Função recursiva para remover um nó da árvore AVL.

        :param raiz: Raiz da subárvore onde o nó será removido.
        :type raiz: Node
        :param chave: A chave do animal a ser removido.
        :type chave: int
        :return: O nó raiz atualizado após a remoção e balanceamento.
        :rtype: Node
        """

        if not raiz:
            return None # Mudar dps
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
        """
        Atualiza um nó na árvore AVL substituindo o nó com a chave antiga por um nó com o novo animal.

        Essa função primeiro remove o nó com a chave antiga e depois insere o nó atualizado.

        :param chave_antiga: A chave (ID do animal) que deve ser substituída.
        :type chave_antiga: int
        :param animal_atualizado: O novo animal que será inserido no lugar do antigo.
        :type animal_atualizado: Animal
        """

        self.remover(chave_antiga)
        self.inserir(animal_atualizado)

    def consultar(self, chave):
        """
        Consulta um nó na árvore AVL com base na chave.

        :param chave: A chave (ID do animal) a ser consultada.
        :type chave: int
        :return: O nó correspondente ao animal ou None se não encontrado.
        :rtype: Node or None
        """

        return self._consultar(self.raiz, chave)

    def _consultar(self, raiz, chave):
        """
        Função recursiva para consultar um nó na árvore AVL.

        :param raiz: Raiz da subárvore onde o nó será consultado.
        :type raiz: Node
        :param chave: A chave (ID do animal) a ser consultada.
        :type chave: int
        :return: O nó correspondente ao animal ou None se não encontrado.
        :rtype: Node or None
        """

        if not raiz or raiz.chave == chave:
            return raiz
        elif chave < raiz.chave:
            return self._consultar(raiz.filho_esquerdo, chave)  # Procura na subárvore esquerda
        else:
            return self._consultar(raiz.filho_direito, chave)  # Procura na subárvore direita

    def _obter_altura(self, node):
        """
        Retorna a altura de um nó.

        :param node: O nó cuja altura será retornada.
        :type node: Node
        :return: A altura do nó.
        :rtype: int
        """

        if not node:
            return 0
        return node.altura

    def _atualizar_altura(self, node):
        """
        Atualiza a altura de um nó com base na altura dos seus filhos.

        :param node: O nó cuja altura será atualizada.
        :type node: Node
        """

        if not node:
            return 0
        node.altura = 1 + max(self._obter_altura(node.filho_esquerdo), self._obter_altura(node.filho_direito))

    def _obter_fator_balanceamento(self, node):
        """
        Calcula o fator de balanceamento de um nó.

        :param node: O nó cujo fator de balanceamento será calculado.
        :type node: Node
        :return: O fator de balanceamento do nó.
        :rtype: int
        """

        if not node:
            return 0
        return self._obter_altura(node.filho_esquerdo) - self._obter_altura(node.filho_direito)  # Calcula o fator de balanceamento do nó

    def _rotacionar_esquerda(self, node):
        """
        Realiza a rotação à esquerda em um nó.

        :param node: O nó sobre o qual será realizada a rotação.
        :type node: Node
        :return: O nó atualizado após a rotação.
        :rtype: Node
        """

        filho_direito = node.filho_direito
        neto = filho_direito.filho_esquerdo

        filho_direito.filho_esquerdo = node
        node.filho_direito = neto

        self._atualizar_altura(node)
        self._atualizar_altura(filho_direito)

        return filho_direito

    def _rotacionar_direita(self, node):
        """
        Realiza a rotação à direita em um nó da árvore AVL.

        Esta rotação é usada para balancear a árvore AVL quando o fator de balanceamento
        do nó é maior que 1 e o fator de balanceamento do filho esquerdo é maior ou igual a 0.

        :param node: O nó que será rotacionado à direita.
        :type node: Node
        :return: O novo nó raiz após a rotação à direita.
        :rtype: Node
        """

        filho_esquerdo = node.filho_esquerdo
        neto = filho_esquerdo.filho_direito

        filho_esquerdo.filho_direito = node
        node.filho_esquerdo = neto

        self._atualizar_altura(node)
        self._atualizar_altura(filho_esquerdo)

        return filho_esquerdo

    def _obter_nó_minimo(self, raiz):
        """
        Encontra o nó com o menor valor (a menor chave) em uma subárvore.

        :param raiz: O nó raiz da subárvore onde o nó mínimo será encontrado.
        :type raiz: Node
        :return: O nó com a menor chave na subárvore.
        :rtype: Node
        """

        minimo = raiz
        while minimo.filho_esquerdo:
            minimo = minimo.filho_esquerdo
        return minimo

    def inorder_traversal(self) -> None:
        with StringIO("") as string_stream:
            self._inorder_traversal(self.raiz, string_stream)
            print(string_stream.getvalue())

    def _inorder_traversal(self, raiz, string_stream : StringIO):
        """
        Percorre a árvore AVL em ordem (in-order) e imprime as informações dos nós.

        :param raiz: O nó raiz da subárvore a ser percorrida.
        :type raiz: Node
        """
        if raiz:
            self._inorder_traversal(raiz.filho_esquerdo, string_stream)  # Percorre a subárvore esquerda
            string_stream.write(
                f"ID: {raiz.animal.id} | APELIDO: {raiz.animal.apelido}\n"
            )
            self._inorder_traversal(raiz.filho_direito, string_stream)  # Percorre a subárvore direita
