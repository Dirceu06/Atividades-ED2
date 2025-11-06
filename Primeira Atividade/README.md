# Primeira Atividade: Algoritmos de Ordenação

Este projeto implementa e compara o desempenho de sete algoritmos de ordenação, analisando o número de comparações e o tempo de execução, conforme especificado no enunciado da Atividade Prática 01.

## Descrição do Enunciado

O objetivo é implementar um programa que receba uma quantidade de números inteiros (N) e o método de geração desses números. O vetor de N posições deve ser preenchido de três formas:
* `'c'`: Crescente (1 a N).
* `'d'`: Decrescente (N a 1).
* `'r'`: Randômico (valores entre 0 e 32000).

O programa deve gerar um arquivo de saída contendo, para cada algoritmo, o nome do método, os elementos ordenados, o tempo gasto e o total de comparações.

## Algoritmos Implementados

O enunciado solicitava 6 métodos básicos mais um método extra à escolha da equipe. Este projeto implementa:
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
* `auxiliar.py`: Funções auxiliares para ler o arquivo de entrada, gerar o vetor e formatar/escrever o arquivo de saída.
* `mainEntrega.py`: Versão monolítica do código (combina todos os módulos) para a entrega da atividade, conforme solicitado.

## Como Usar

1.  Prepare um arquivo de entrada (ex: `entrada.txt`) com duas linhas:
    * *Linha 1:* O tamanho (N) do vetor.
    * *Linha 2:* O modo ('c', 'd' ou 'r').

2.  Execute o script principal, passando o arquivo de entrada e o de saída como argumentos:

    ```bash
    python main.py entrada.txt saida.txt
    ```

3.  Os resultados detalhados de cada algoritmo serão salvos em `saida.txt`.