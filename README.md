# Gerenciador-de-Fauna

Projeto que permite o armazenamento, consulta e atualização de informações sobre animais.

## Execução do programa

Para executar o programa, você pode fornecer o caminho do arquivo como um argumento de linha de comando ou inseri-lo quando solicitado.

### Comando de linha

\`\`\`bash
python3 main.py /caminho/do/arquivo
\`\`\`

### Solicitação interativa

\`\`\`bash
python3 main.py
Digite o caminho do arquivo: /caminho/do/arquivo
\`\`\`

Certifique-se de substituir \`/caminho/do/arquivo\` pelo caminho real do arquivo que você deseja usar.

## Descrição do Programa

Este programa permite que você armazene informações sobre animais em um arquivo e realize operações como adicionar novos animais, visualizar a lista de animais e atualizar as informações de um animal existente.

O arquivo deve estar em formato de texto simples e seguir um padrão específico para que o programa possa ler e escrever corretamente os dados.

## Formato do Arquivo

O arquivo de entrada deve seguir o seguinte formato:

\`\`\`
<id>, <apelido_do_animal>, <data_de_inicio_do_monitoramento>, <especie>, <sexo>, <data_nascimento>, <data_da_avaliacao>, <temperatura>, <peso>, <altura>, <teve_amostra?>, <exame_ok?>, <problema_de_saude>
\`\`\`

Cada linha no arquivo representa um animal, com o as informações separadas por vírgulas.

## Exemplo de Uso

Suponha que temos um arquivo chamado \`animais.txt\` com o seguinte conteúdo:

\`\`\`
1, Feijão, 2022-01-01, Arara Verde, M, 2019-05-15, 2022-06-30, 37.5, 200, 120, Sim, Sim, None
2, Rex, 2022-02-15, Iguana, M, 2018-11-20,2009-12-24,39,100,900,Sim,Não,Irritação
3, Lulu, 2022-03-10, Jibóia, F, 2020-02-10, 2022-08-10, 37.2, 800, 500, Não, Não, Gripe
4, Bob, 2022-04-05, Sagui, M, 2021-07-01, 2022-09-20, 38.2, 250, 100, Sim, Sim, None
5, Lua, 2022-05-20, Jaguatirica, F, 2020-12-05, 2022-10-05, 36.5, 10, 40, Não, Sim, None
\`\`\`

Podemos executar o programa da seguinte maneira:

\`\`\`bash
python3 main.py animais.txt
\`\`\`

Isso carregará os animais do arquivo \`animais.txt\` e permitirá que você realize operações sobre eles.
