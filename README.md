# Gerenciador-de-Fauna

Projeto que permite o armazenamento, consulta e atualização de informações sobre animais.

## Execução do programa

Para executar o programa, você pode fornecer o caminho do arquivo como um argumento de linha de comando ou inseri-lo quando solicitado.

### Comando de linha

```bash
python3 /source/main.py /caminho/do/arquivo
```

Para usar o arquivo de teste providenciado, utilize:

```bash
python3 /source/main.py /data/fauna.json
```

### Solicitação interativa

```
python3 /source/main.py
Digite o caminho do arquivo: /caminho/do/arquivo
```

Certifique-se de substituir \`/caminho/do/arquivo\` pelo caminho real do arquivo que você deseja usar.

## Descrição do Programa

Este programa permite que você armazene informações sobre animais em um arquivo e realize operações como adicionar novos animais, visualizar a lista de animais e atualizar as informações de um animal existente.

O arquivo deve estar em formato JSON e seguir um padrão específico para que o programa possa ler e escrever corretamente os dados.

## Formato do Arquivo

O arquivo de entrada deve seguir o seguinte formato:

O arquivo JSON segue a seguinte estrutura:

- **animals**: Uma lista que contém objetos representando diferentes animais.
  - **id**: Um número inteiro que identifica exclusivamente o animal.
  - **apelido**: Uma string que representa o apelido do animal.
  - **inicio_monitoramento**: Uma string que indica a data de início do monitoramento do animal no formato "dd/mm/aaaa".
  - **especie**: Uma string que especifica a espécie do animal.
  - **sexo**: Uma string que representa o sexo do animal (M para masculino, F para feminino).
  - **data_nascimento**: Uma string que indica a data de nascimento do animal no formato "dd/mm/aaaa".
  - **historico**: Uma lista que contém objetos representando o histórico de avaliações médicas do animal.
    - **data_avaliacao**: Uma string que indica a data da avaliação médica no formato "dd/mm/aaaa".
    - **temperatura**: Um número que representa a temperatura corporal do animal na avaliação médica.
    - **peso**: Um número que representa o peso do animal na avaliação médica.
    - **altura**: Um número que representa a altura do animal na avaliação médica.
    - **amostra**: Um booleano que indica se uma amostra foi coletada durante a avaliação médica.
    - **exame**: Um booleano que indica se o exame físico está ok.
    - **problema_saude**: Uma string que descreve qualquer problema de saúde detectado durante a avaliação médica, ou `null` se nenhum problema foi detectado.

A leitura e salvamento dos arquivos seguem esse mesmo formato.

## Exemplo de Arquivo

```
{
    "animals": [
        {
            "id": 1,
            "apelido": "Leo",
            "inicio_monitoramento": "01/01/2022",
            "especie": "Lion",
            "sexo": "M",
            "data_nascimento": "15/05/2019",
            "historico": [
                {
                    "data_avaliacao": "15/02/2022",
                    "temperatura": 37.5,
                    "peso": 150,
                    "altura": 180,
                    "amostra": true,
                    "exame": true,
                    "problema_saude": null
                },
                {
                    "data_avaliacao": "20/03/2022",
                    "temperatura": 38.2,
                    "peso": 148,
                    "altura": 175,
                    "amostra": false,
                    "exame": false,
                    "problema_saude": null
                }
            ]
        },
        {
            "id": 2,
            "apelido": "Molly",
            "inicio_monitoramento": "01/01/2022",
            "especie": "Elephant",
            "sexo": "F",
            "data_nascimento": "10/10/2015",
            "historico": [
                {
                    "data_avaliacao": "15/02/2022",
                    "temperatura": 36.8,
                    "peso": 5000,
                    "altura": 300,
                    "amostra": true,
                    "exame": true,
                    "problema_saude": null
                },
                {
                    "data_avaliacao": "20/03/2022",
                    "temperatura": 37.2,
                    "peso": 4800,
                    "altura": 290,
                    "amostra": true,
                    "exame": false,
                    "problema_saude": "Infecção urinária"
                }
            ]
        }
    ]
}
```
