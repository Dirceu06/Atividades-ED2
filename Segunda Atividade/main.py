import sys
import leitura
import sorts
import auxiliar

def main():
    herois, sortMethode, orderMethode = leitura.lerArquivo(sys.argv)   
    try:
        saida=sys.argv[2]
    except IndexError:
        saida="output.txt"
        
    if sortMethode == -1 or orderMethode == -1:
        sys.exit('Encerrando programa com erro')    
    heroisOrdenado = []    
    if sortMethode in 'iI':
        heroisOrdenado = sorts.insertionSort(herois,orderMethode)
    elif sortMethode in 'mM':
        heroisOrdenado = sorts.mergeSort(herois,orderMethode)
    elif sortMethode in 'qQ':
        heroisOrdenado = sorts.quickSort(herois,orderMethode)
    else:
        heroisOrdenado = sorts.heapSort(herois,orderMethode)
    auxiliar.reescreverReg(heroisOrdenado,herois,saida)

if __name__ == "__main__":
    main()
