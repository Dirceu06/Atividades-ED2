# Atividade Prática 04: Estruturas de Índices - Spotify 1.2M+ Songs

Este projeto implementa uma solução de **Índices Secundários** para realizar buscas eficientes em uma base de dados de músicas do Spotify, contendo mais de 1.2 milhão de registros. O desenvolvimento atende aos requisitos da disciplina de Estrutura de Dados 2 (UTFPR).

## Descrição do Enunciado

O objetivo é desenvolver um programa que crie índices secundários para permitir consultas rápidas em um arquivo CSV de grande porte. O sistema deve ser capaz de processar consultas simples (um campo) e consultas compostas com operadores booleanos (AND/OR), retornando as músicas que correspondem aos critérios especificados sem a necessidade de varrer o arquivo inteiro linearmente para cada busca.

## Dataset

O projeto utiliza o dataset "Spotify 1.2M+ Songs". Devido ao tamanho do arquivo, ele deve ser baixado separadamente através do link abaixo:

* **Download do Dataset (1.2M registros):** [spotify-1M.csv](https://drive.google.com/file/d/18ZFCDbLKzxB0mbTIPVdxUoq8xlXb5uGu/view?usp=sharing)

## Funcionalidades

* **Leitura de Dados:** Carrega e processa o arquivo `spotify-1M.csv`, tratando os campos de tamanho variável separados por vírgula.
* **Criação de Índices:** Gera índices secundários em memória para os campos solicitados na consulta.
* **Processamento de Consultas (`query`):**
    * **Consulta Simples:** Busca baseada em um único campo (ex: apenas `artist_name`).
    * **Consulta Booleana:** Suporta operadores lógicos para combinar múltiplos campos:
        * `&` (AND): Interseção de resultados (ex: Artista X **E** Ano Y).
        * `||` (OR): União de resultados (ex: Artista X **OU** Artista Y).
* **Saída Formatada:** Gera um arquivo de saída contendo apenas os registros completos das músicas encontradas.
* **Controle de Erros:** Tratamento para arquivos vazios, nomes de campos inválidos, falha na abertura de arquivos e argumentos de linha de comando incorretos.

## Estrutura dos Arquivos

Conforme solicitado nas instruções de entrega, o código deve ser consolidado, mas a lógica opera sobre os seguintes tipos de arquivo:

* `main.py/leituraEescrita.py`: Script principal contendo a lógica de leitura, indexação e busca.
* `spotify-1M.csv`: Base de dados de entrada (deve estar na mesma pasta ou no caminho indicado).
* `query.txt`: Arquivo de entrada contendo a definição da busca (campos e valores).
* `output.txt`: Arquivo gerado pelo programa com os resultados da busca.

## Como Usar

1.  Baixe o dataset `spotify-1M.csv` no link fornecido acima.

2.  Prepare um arquivo de consulta (ex: `query.txt`) seguindo o formato:
    * *Exemplo Simples:*
        ```text
        name
        The Number of the Beast
        ```
    * *Exemplo Booleano (AND):*
        ```text
        artists & year & name
        Rage Against The Machine, 1992, Bombtrack
        ```

3.  Execute o script via terminal passando os 3 argumentos obrigatórios (dataset, arquivo de query e arquivo de saída):

    ```bash
    python main.py spotify-1M.csv query.txt saida.txt
    ```

4.  Verifique o arquivo `saida.txt`. Ele conterá as linhas completas do CSV correspondentes às músicas encontradas ou uma mensagem de erro/aviso caso nada seja encontrado.