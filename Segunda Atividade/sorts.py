import auxiliar
# heapSort
def maxHeapify(vetor, i, n, op):
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    maior = i

    if op:  # ordem decrescente
        if esquerda < n and vetor[esquerda][0] < vetor[maior][0]:
            maior = esquerda
        if direita < n and vetor[direita][0] < vetor[maior][0]:
            maior = direita
    else:   # ordem crescente
        if esquerda < n and vetor[esquerda][0] > vetor[maior][0]:
            maior = esquerda
        if direita < n and vetor[direita][0] > vetor[maior][0]:
            maior = direita

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        maxHeapify(vetor, maior, n, op)


def buildHeap(vetor, op):
    n = len(vetor)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(vetor, i, n, op)


def heapSort(herois, op=False):
    vetor = auxiliar.gerarVetorKeyEpos(herois)
    n = len(vetor)
    buildHeap(vetor, op)
    for i in range(n - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        maxHeapify(vetor, 0, i, op)
    return vetor

# quickSort
def quickSort(herois,op=False):
    vetor = auxiliar.gerarVetorKeyEpos(herois)
    quickSortVerdadeiro(vetor,0,len(vetor)-1,op)
    return vetor

def quickSortVerdadeiro(vetor, inicio, fim, op=False):
    if inicio < fim:
        pivo = particionaQuickSort(vetor, inicio, fim, op)
        quickSortVerdadeiro(vetor, inicio, pivo-1,op)
        quickSortVerdadeiro(vetor, pivo+1, fim,op)    

def particionaQuickSort(vetor, inicio, fim,op):
    esquerda = inicio
    direita = fim
    pivoComp = vetor[inicio][0]

    while esquerda < direita:
        if op:
            while esquerda <=fim and vetor[esquerda][0] >= pivoComp :
                esquerda += 1
            while  direita > inicio and vetor[direita][0] < pivoComp :
                direita -= 1
            if esquerda < direita:
                vetor[esquerda], vetor[direita] = vetor[direita],vetor[esquerda]
        else:
            while vetor[esquerda][0] <= pivoComp and esquerda <=fim:
                esquerda += 1
            while vetor[direita][0] > pivoComp and direita > inicio:
                direita -= 1
            if esquerda < direita:
                vetor[esquerda], vetor[direita] = vetor[direita],vetor[esquerda]
    vetor[inicio], vetor[direita] = vetor[direita],vetor[inicio]
    return direita

#mergeSort
def mergeSort(herois, op=False):
    vet = auxiliar.gerarVetorKeyEpos(herois)
    mergeSortVerdadeiro(vet, 0, len(vet) - 1, op)
    return vet


def mergeSortVerdadeiro(vet, inicio, fim, op=False):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergeSortVerdadeiro(vet, inicio, meio, op)
        mergeSortVerdadeiro(vet, meio + 1, fim, op)
        merge(vet, inicio, meio, fim, op)


def merge(vet, inicio, meio, fim, op):
    aux = []
    p1 = inicio
    p2 = meio + 1

    while p1 <= meio and p2 <= fim:
        if op: 
            if vet[p1][0] > vet[p2][0]:
                aux.append(vet[p1])
                p1 += 1
            else:
                aux.append(vet[p2])
                p2 += 1
        else:
            if vet[p1][0] < vet[p2][0]:
                aux.append(vet[p1])
                p1 += 1
            else:
                aux.append(vet[p2])
                p2 += 1

    while p1 <= meio:
        aux.append(vet[p1])
        p1 += 1

    while p2 <= fim:
        aux.append(vet[p2])
        p2 += 1

    # copia de volta pro vetor original
    for i in range(len(aux)):
        vet[inicio + i] = aux[i]


#insertionSort
# recebe vetor de herois e ele mesmo cria vetor para reescrever
def insertionSort(herois, op=False):
    vet=auxiliar.gerarVetorKeyEpos(herois)
    for i in range(1, len(vet)):
        k = i - 1
        aux = vet[i]
        if not op:  # crescente
            while k >= 0 and aux[0] < vet[k][0]:
                vet[k + 1] = vet[k]
                k -= 1
        else:  # decrescente
            while k >= 0 and aux[0] > vet[k][0]:
                vet[k + 1] = vet[k]
                k -= 1
        vet[k + 1] = aux
    return vet
