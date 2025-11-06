import time

def bubbleSort(lista):
    inicio = time.time()
    comparacoes = 0
    
    troca = True
    j = len(lista)-1
    while(troca):
        troca = False
        for i in  range(j):
            comparacoes += 1
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1], lista[i]
                troca = True
        j -= 1
    fim =time.time()
    timer = fim-inicio
    return lista, comparacoes, timer

def selectionSort(lista):
    inicio = time.time() 
    comparacoes = 0
    n = len(lista)
    
    for i in range(0, n-1):
        menor = i
        for j in range(i+1, n):   
            comparacoes += 1   
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[menor], lista[i] = lista[i], lista[menor]
        
    fim = time.time()
    timer = fim - inicio
    return lista, comparacoes, timer

def insertionSort(lista):
    inicio = time.time()
    comparacoes = 0
    for i in range(1,len(lista)):
        k = i - 1
        aux = lista[i]
        while k >= 0:
            comparacoes += 1  
            if aux < lista[k]:
                comparacoes += 1  
                lista[k+1] = lista[k]
                k -= 1
            else:
                break
        lista[k + 1] = aux
    fim = time.time()
    timer = fim-inicio
    return lista, comparacoes, timer

comparacoesMergeSort = 0

def mergeSortVerdadeiro(lista, inicio, fim):
    global comparacoesMergeSort
    
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergeSortVerdadeiro(lista, inicio, meio)
        mergeSortVerdadeiro(lista, meio + 1, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    global comparacoesMergeSort
    aux = []
    p1 = inicio
    p2 = meio + 1
    
    while p1 <= meio and p2 <= fim:
        comparacoesMergeSort += 1
        if lista[p1] < lista[p2]:
            aux.append(lista[p1])
            p1 += 1
        else:
            aux.append(lista[p2])
            p2 += 1

    aux.extend(lista[p1:meio+1])
    aux.extend(lista[p2:fim+1])
        
    for i in range(len(aux)):
        lista[inicio + i] = aux[i]

def mergeSort(lista):
    global comparacoesMergeSort
    comparacoesMergeSort = 0
    
    inicio_tempo = time.time()
    mergeSortVerdadeiro(lista, 0, len(lista) - 1)
    fim_tempo = time.time()
    
    return lista, comparacoesMergeSort, fim_tempo - inicio_tempo

def quick(vetor):
    global comparacoesQuickSort
    comparacoesQuickSort = 0
    inicio_tempo = time.time()
    quickVerdadeiro(vetor,0,len(vetor)-1)
    fim_tempo = time.time()
    
    return vetor, comparacoesQuickSort, fim_tempo - inicio_tempo
    
def quickVerdadeiro(vetor,inicio,fim):
    if inicio < fim:
        pivo = particiona(vetor,inicio,fim)
        quickVerdadeiro(vetor,inicio,pivo-1)
        quickVerdadeiro(vetor,pivo+1,fim)
        
def particiona(vetor,inicio,fim):
    global comparacoesQuickSort
    esquerda = inicio
    direita = fim
    pivo = vetor[inicio]
   
    while esquerda < direita:
        while esquerda < fim and vetor[esquerda] <= pivo:
            comparacoesQuickSort+=1
            esquerda+=1
            
        while  direita > inicio and vetor[direita] > pivo:
            comparacoesQuickSort+=1
            direita-=1
            
        if esquerda < direita:
            vetor[esquerda],vetor[direita]=vetor[direita],vetor[esquerda]
            
    vetor[inicio],vetor[direita]=vetor[direita],vetor[inicio]
    return direita

comparacoesHeapSort = 0

def maxHeapfy(lista, i, n, ):
    global comparacoesHeapSort
    esquerda = 2*i + 1
    direita = 2*i + 2
    maior = i

    
    if esquerda < n:
        comparacoesHeapSort += 1
        if lista[esquerda] > lista[maior]:
            maior = esquerda
    if direita < n:
        comparacoesHeapSort += 1
        if lista[direita] > lista[maior]:
            maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        maxHeapfy(lista, maior, n, )


def buildMaxHeap(lista, ):
    n = len(lista)
    for i in range((n // 2) - 1, -1, -1):
        maxHeapfy(lista, i, n, )


def heapSort(lista):
    global comparacoesHeapSort
    comparacoesHeapSort = 0
    inicio_tempo = time.time()

    n = len(lista)
    buildMaxHeap(lista, )
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        maxHeapfy(lista, 0, i, )

    fim_tempo = time.time()
    return lista, comparacoesHeapSort, fim_tempo - inicio_tempo

def cocktailSort(lista):
    inicio_tempo = time.time()
    comparacoes = 0
    n = len(lista)
    troca = True
    inicio = 0
    fim = n - 1
    
    while troca:
        troca = False
        for i in range(inicio, fim):
            comparacoes += 1
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                troca = True
        
        if not troca:
            break  
            
        troca = False
        fim -= 1  
        
        for i in range(fim - 1, inicio - 1, -1):
            comparacoes += 1
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                troca = True
                
        inicio += 1  
    
    fim_tempo = time.time()
    return lista, comparacoes, fim_tempo - inicio_tempo