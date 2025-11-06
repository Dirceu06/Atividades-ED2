# [cite_start]Segunda Atividade: Keysorting - Marvel/DC Heroes [cite: 4]

[cite_start]Este projeto implementa uma solução de *Keysorting* para classificar uma base de dados de heróis, lida de um arquivo `.txt`, conforme especificado no enunciado da Atividade Prática 02[cite: 4].

## Descrição do Enunciado

[cite_start]O objetivo é implementar uma solução que ordene um arquivo com informações de heróis[cite: 20]. [cite_start]O desafio é implementar o método *Keysorting* [cite: 21][cite_start], que reaproveita conceitos de algoritmos de ordenação tradicionais[cite: 22]. [cite_start]O programa deve ler um arquivo de entrada, ordenar os registros com base na chave (`key`) e gravar o resultado em um novo arquivo ordenado[cite: 23].

## Funcionalidades

* [cite_start]Lê um arquivo de entrada que contém dados de heróis [cite: 104][cite_start], com campos separados pelo caractere pipe (`|`)[cite: 120].
* [cite_start]Processa a **primeira linha** do arquivo para determinar o método de ordenação (`SORT=`) e a ordem (`ORDER=`)[cite: 110].
* [cite_start]**Métodos (`SORT`):** São aceitas 4 opções[cite: 114]:
    * `'I'` - Insertion Sort
    * `'M'` - Merge Sort
    * `'Q'` - Quick Sort
    * `'H'` - Heap Sort
* [cite_start]**Ordem (`ORDER`):** São aceitas 2 opções[cite: 116]:
    * `'C'` - Crescente
    * `'D'` - Decrescente
* [cite_start]Processa a **segunda linha** como o cabeçalho dos atributos (key, Name, etc.)[cite: 117, 134].
* [cite_start]Ordena os dados com base na `key` (chave) de cada herói[cite: 21, 135].
* [cite_start]Escreve os dados ordenados em um arquivo de saída, incluindo a linha de cabeçalho dos campos[cite: 129, 136].
* [cite_start]Implementa controle de erros para casos como arquivos inválidos ou vazios[cite: 144, 145, 147, 148].

## Estrutura dos Arquivos

* [cite_start]`main.py`: Script principal que coordena a leitura [cite: 157] e chama o algoritmo de ordenação correto.
* [cite_start]`leitura.py`: Define a classe `Heroi` [cite: 121] e contém a lógica para ler, validar e processar o arquivo de entrada.
* [cite_start]`sorts.py`: Contém a implementação dos 4 algoritmos de ordenação (Insertion, Merge, Quick, Heap) adaptados para o Keysorting[cite: 114].
* `auxiliar.py`: Funções auxiliares para manipulação dos dados (gerar vetor de chaves/índices e reescrever o arquivo de saída formatado).
* [cite_start]`mainentrega.py`: Versão monolítica do código para entrega, combinando todos os módulos em um único arquivo, conforme solicitado[cite: 14, 15, 167].

## Como Usar

1.  [cite_start]Prepare um arquivo de entrada (ex: `herois.txt`) com o formato especificado[cite: 104]:
    * [cite_start]*Linha 1:* `SORT=M,ORDER=C` (Exemplo para Merge Sort crescente)[cite: 110, 111].
    * [cite_start]*Linha 2:* O cabeçalho dos dados (ex: `key,Name,Alignment,...Total`)[cite: 117].
    * [cite_start]*Linhas 3+:* Os dados dos heróis, com atributos separados por `|`[cite: 120].

2.  [cite_start]Execute o script principal, passando o arquivo de entrada e o de saída como argumentos[cite: 140]:

    ```bash
    python main.py herois.txt saida_ordenada.txt
    ```

3.  [cite_start]Os dados dos heróis, ordenados pela `key`, serão salvos em `saida_ordenada.txt`[cite: 129].