import ordenadores
import auxiliar
import sys

definicoes = auxiliar.lerArq(sys.argv)
    
if definicoes == -1:
    sys.exit('Encerrando programa com erro')
gerado = auxiliar.gerarVetor(definicoes[0],definicoes[1])

algoritmos = [
    ("selection", ordenadores.selectionSort),
    ("bubble", ordenadores.bubbleSort), 
    ("insertion", ordenadores.insertionSort),
    ("merge", ordenadores.mergeSort),
    ("quick", ordenadores.quick),
    ("heap", ordenadores.heapSort),
    ("cocktail", ordenadores.cocktailSort)
]

linhas = [auxiliar.formatar_linha_ordenacao(nome, funcao(gerado[:]), definicoes[0]) 
          for nome, funcao in algoritmos]
    
print(gerado)
print('-='*38,end='-\n')
for i in linhas: print(i)
print('-='*38,end='-\n')
auxiliar.escreverArq(linhas)