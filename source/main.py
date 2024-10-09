import sys
from manager import initialize

# Verifica se o caminho do arquivo foi passado como argumento  na linha de comando
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = input("Digite o caminho do arquivo: ")

# Inicializa aplicação com o caminho do arquivo
initialize(file_path)
