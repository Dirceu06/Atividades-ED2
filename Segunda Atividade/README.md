# Segunda Atividade: Keysorting - Marvel/DC Heroes

Este projeto implementa uma solução de *Keysorting* para classificar uma base de dados de heróis, lida de um arquivo `.txt`, conforme especificado no enunciado da Atividade Prática 02.

## Descrição do Enunciado

O objetivo é implementar uma solução que ordene um arquivo com informações de heróis. O desafio é implementar o método *Keysorting*, que reaproveita conceitos de algoritmos de ordenação tradicionais. O programa deve ler um arquivo de entrada, ordenar os registros com base na chave (`key`) e gravar o resultado em um novo arquivo ordenado.

## Funcionalidades

* Lê um arquivo de entrada que contém dados de heróis, com campos separados pelo caractere pipe (`|`).
* Processa a **primeira linha** do arquivo para determinar o método de ordenação (`SORT=`) e a ordem (`ORDER=`).
* **Métodos (`SORT`):** São aceitas 4 opções:
    * `'I'` - Insertion Sort
    * `'M'` - Merge Sort
    * `'Q'` - Quick Sort
    * `'H'` - Heap Sort
* **Ordem (`ORDER`):** São aceitas 2 opções:
    * `'C'` - Crescente
    * `'D'` - Decrescente
* Processa a **segunda linha** como o cabeçalho dos atributos (key, Name, etc.).
* Ordena os dados com base na `key` (chave) de cada herói.
* Escreve os dados ordenados em um arquivo de saída, incluindo a linha de cabeçalho dos campos.
* Implementa controle de erros para casos como arquivos inválidos ou vazios.

## Estrutura dos Arquivos

* `main.py`: Script principal que coordena a leitura e chama o algoritmo de ordenação correto.
* `leitura.py`: Define a classe `Heroi` e contém a lógica para ler, validar e processar o arquivo de entrada.
* `sorts.py`: Contém a implementação dos 4 algoritmos de ordenação (Insertion, Merge, Quick, Heap) adaptados para o Keysorting.
* `auxiliar.py`: Funções auxiliares para manipulação dos dados (gerar vetor de chaves/índices e reescrever o arquivo de saída formatado).
* `mainentrega.py`: Versão monolítica do código para entrega, combinando todos os módulos em um único arquivo, conforme solicitado.

## Como Usar

1.  Prepare um arquivo de entrada (ex: `herois.txt`) com o formato especificado:
    * *Linha 1:* `SORT=M,ORDER=C` (Exemplo para Merge Sort crescente).
    * *Linha 2:* O cabeçalho dos dados (ex: `key,Name,Alignment,...Total`).
    * *Linhas 3+:* Os dados dos heróis, com atributos separados por `|`.

2.  Execute o script principal, passando o arquivo de entrada e o de saída como argumentos:

    ```bash
    python main.py herois.txt saida_ordenada.txt
    ```

3.  Os dados dos heróis, ordenados pela `key`, serão salvos em `saida_ordenada.txt`.