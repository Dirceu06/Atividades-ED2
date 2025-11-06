import sys

class Heroi:
    def __init__(self, key, nome, alinhamento, genero, olhosCor, race, cabeloCor, editora, corDePele, altura,
                peso, inteligencia, forca, velocidade, durabilidade, poder, combate, total):
        self.key = key
        self.nome = nome
        self.alinhamento = alinhamento
        self.genero = genero
        self.olhosCor = olhosCor
        self.race = race
        self.cabeloCor = cabeloCor
        self.editora = editora
        self.corDePele = corDePele
        self.altura = altura
        self.peso = peso
        self.inteligencia = inteligencia
        self.forca = forca
        self.velocidade = velocidade
        self.durabilidade = durabilidade
        self.poder = poder
        self.combate = combate
        self.total = total
        
       
def lerArquivo(parametros):
    if len(parametros) < 2:
        sys.exit('Encerrando programa com erro') 
    try:
        arquivo = parametros[1]
        saida = parametros[2] if len(parametros) > 2 else "output.txt"
        
        with open(arquivo, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()
            
            if not linhas:
                reescreverReg(0, 0, saida, False)
                print("Arquivo Vazio")
                sys.exit('Encerrando programa com erro')
            
            if len(linhas) < 3:
                reescreverReg(0, 0, saida, False)
                print("Arquivo com formato inválido - faltam linhas")
                sys.exit('Encerrando programa com erro')
            
            cabecalho_arquivo = linhas[1].strip()
            cabecalho = "key,Name,Alignment,Gender,EyeColor,Race,HairColor,Publisher,SkinColor,Height,Weight,Intelligence,Strength,Speed,Durability,Power,Combat,Total"
            if cabecalho_arquivo != cabecalho:
                reescreverReg(0, 0, saida, False)
                print("Arquivo Invalido")
                sys.exit('Encerrando programa com erro')        

        sort, order = lerLetras(linhas[0])
        herois = alocarHerois(linhas[2:])  # começa na linha 3
        
        if not herois:
            reescreverReg(0, 0, saida, False)
            print("Nenhum herói encontrado para ordenar")
            sys.exit('Encerrando programa com erro')
            
        if sort not in 'qQmMhHiI':
            sort = -1
        if order not in 'cCdD':
            order = -1
        else:
            if order not in 'cC':
                order = True
            else:
                order = False

        return herois, sort, order, saida

    except FileNotFoundError:
        saida = parametros[2] if len(parametros) > 2 else "output.txt"
        print(f"Arquivo {arquivo} não encontrado.")
        reescreverReg(0, 0, saida, False)
        sys.exit('Encerrando programa com erro')

def alocarHerois(linhas):
    herois = []
    for linha in linhas:
        linha = linha.strip()
        
        if not linha:
            continue
            
        linha = linha.replace("||", "|-|")  # preenche campos vazios
        atributos = linha.strip().split('|')

        if len(atributos) < 18:
            atributos += ["-"] * (18 - len(atributos))

        heroi = Heroi(*atributos[:18])
        herois.append(heroi)
    return herois

def lerLetras(linhaCabecalho):
    """
    Espera uma linha no formato: SORT=M,ORDER=C
    Retorna sort='M', order='C'
    """
    cabecalho = linhaCabecalho.strip()
    partes = cabecalho.split(',')
    
    if len(partes) < 2:
        return -1, -1
        
    try:
        sort = partes[0].split('=')[1]
        order = partes[1].split('=')[1]
        return sort, order
    except IndexError:
        return -1, -1

def gerarVetorKeyEpos(herois : list[Heroi]):
    vet = list()
    for i in range(len(herois)):
        try:
            aux = [int(herois[i].key), i]
            vet.append(aux)
        except ValueError:
            aux = [0, i]
            vet.append(aux)
    return vet

def HeroiclassParaLinha(heroi : Heroi):
    atributos = vars(heroi)           
    valores = []    
                     
    for valor in atributos.values(): 
        valores.append(str(valor))    

    linha = "|".join(valores) + "\n" 
    return linha

def reescreverReg(vet=0, herois=0, arquivo="output.txt", funcionou=True):
    try:
        with open(arquivo, "w", encoding="utf-8") as arq:
            if funcionou:
                if len(vet) != len(herois):
                    print("reescrever reg erro!!!")
                    return
                linhas = list()
                linha = "key,Name,Alignment,Gender,EyeColor,Race,HairColor,Publisher,SkinColor,Height,Weight,Intelligence,Strength,Speed,Durability,Power,Combat,Total\n"
                linhas.append(linha)
                for i in range(len(herois)):
                    linha = HeroiclassParaLinha(herois[vet[i][1]])
                    linhas.append(linha)
                arq.writelines(linhas)
            else:
                linhas = "Arquivo com erro"
                arq.writelines(linhas)
    except Exception as e:
        print(f"Erro ao escrever arquivo: {e}")

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
    vetor = gerarVetorKeyEpos(herois)
    n = len(vetor)
    buildHeap(vetor, op)
    for i in range(n - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        maxHeapify(vetor, 0, i, op)
    return vetor

# quickSort
def quickSort(herois,op=False):
    vetor = gerarVetorKeyEpos(herois)
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
    vet = gerarVetorKeyEpos(herois)
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
    vet=gerarVetorKeyEpos(herois)
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

def main():
    try:
        herois, sortMethode, orderMethode, saida = lerArquivo(sys.argv)
            
        if sortMethode == -1 or orderMethode == -1:
            reescreverReg(0, 0, saida, False)
            sys.exit('Encerrando programa com erro')    
            
        heroisOrdenado = []    
        if sortMethode in 'iI':
            heroisOrdenado = insertionSort(herois, orderMethode)
        elif sortMethode in 'mM':
            heroisOrdenado = mergeSort(herois, orderMethode)
        elif sortMethode in 'qQ':
            heroisOrdenado = quickSort(herois, orderMethode)
        else:
            heroisOrdenado = heapSort(herois, orderMethode)
        reescreverReg(heroisOrdenado, herois, saida)
        
    except Exception as e:
        saida = sys.argv[2] if len(sys.argv) > 2 else "output.txt"
        print(f"Erro durante execução: {e}")
        reescreverReg(0, 0, saida, False)
        sys.exit('Encerrando programa com erro')

if __name__ == "__main__":
    main()