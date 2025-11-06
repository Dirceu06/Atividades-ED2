# [cite_start]Primeira Atividade: Algoritmos de Ordenação [cite: 189]

[cite_start]Este projeto implementa e compara o desempenho de sete algoritmos de ordenação, analisando o número de comparações e o tempo de execução, conforme especificado no enunciado da Atividade Prática 01[cite: 189].

## Descrição do Enunciado

[cite_start]O objetivo é implementar um programa que receba uma quantidade de números inteiros (N) e o método de geração desses números[cite: 203]. [cite_start]O vetor de N posições deve ser preenchido de três formas[cite: 204]:
* [cite_start]`'c'`: Crescente (1 a N)[cite: 205].
* [cite_start]`'d'`: Decrescente (N a 1)[cite: 206].
* [cite_start]`'r'`: Randômico (valores entre 0 e 32000)[cite: 207].

[cite_start]O programa deve gerar um arquivo de saída contendo, para cada algoritmo, o nome do método, os elementos ordenados, o tempo gasto e o total de comparações[cite: 208, 217, 218, 219, 220, 221].

## Algoritmos Implementados

[cite_start]O enunciado solicitava 6 métodos básicos [cite: 209] [cite_start]mais um método extra à escolha da equipe[cite: 210]. Este projeto implementa:
1.  Selection Sort
2.  Bubble Sort
3.  Insertion Sort
4.  Merge Sort
5.  Quick Sort
6.  Heap Sort
7.  Cocktail Sort (método extra)

## Estrutura dos Arquivos

* `main.py`: Script principal que orquestra a leitura, geração, ordenação e escrita.
* `ordenadores.py`: Contém a implementação dos 7 algoritmos de ordenação e a medição de tempo/comparações.
* [cite_start]`auxiliar.py`: Funções auxiliares para ler o arquivo de entrada [cite: 214, 215][cite_start], gerar o vetor [cite: 204] [cite_start]e formatar/escrever o arquivo de saída[cite: 216].
* [cite_start]`mainEntrega.py`: Versão monolítica do código (combina todos os módulos) para a entrega da atividade, conforme solicitado[cite: 200, 270].

## Como Usar

1.  [cite_start]Prepare um arquivo de entrada (ex: `entrada.txt`) com duas linhas[cite: 214]:
    * [cite_start]*Linha 1:* O tamanho (N) do vetor[cite: 214].
    * [cite_start]*Linha 2:* O modo ('c', 'd' ou 'r')[cite: 215].

2.  [cite_start]Execute o script principal, passando o arquivo de entrada e o de saída como argumentos[cite: 238]:

    ```bash
    python main.py entrada.txt saida.txt
    ```

3.  [cite_start]Os resultados detalhados de cada algoritmo serão salvos em `saida.txt`[cite: 216].