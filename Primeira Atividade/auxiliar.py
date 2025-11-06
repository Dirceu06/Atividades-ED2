import random
import sys
def lerArq(nome):
    if len(nome) != 3:
        return -1
    try:
        f = open(nome[1], "r")
        try:
            numero = int(f.readline().strip())
        except ValueError:
            print(f'Número no arquivo de entrada não é inteiro')
            return -1
        caractere = f.readline().strip()
        f.close()
        info = (numero,caractere)
        return info
    except FileNotFoundError:
        print('não existe o arquivo')
        return -1
        
def gerarVetor(tamanho,modo):
    vetor = list()
    if modo in 'cC':
        for i in range(tamanho):
            vetor.append(i)
    elif modo in 'dD':
        for i in range(tamanho,0,-1):
            vetor.append(i)
    elif modo in 'rR':
        for i in range(tamanho):
            vetor.append(random.randint(0,32000))
    else:
        print('não existe')
        return 0
    return vetor

def escreverArq(linhas):
    try:
        arq = open(sys.argv[2], 'w')
    except IndexError:
        arq = open('output.txt', 'w')
    finally:
        arq.write('-='*38+'-\n')
        for i in linhas:
            i = i+'\n'
            arq.write(i)
        arq.write('-='*38+'-\n')
        
def formatar_linha_ordenacao(nome_algoritmo, resultado_ordenacao, qtd):
    vetor_ordenado, comp_info, timer = resultado_ordenacao
    
    vetor_str = f"{' '.join(map(str, vetor_ordenado))}"
    if qtd < 10:
        linha = (f"{nome_algoritmo + ':':^10} {vetor_str} "
                f"comparadorado: {comp_info:^7} vez(es) | "
                f"tempo: {timer * 1000000:^7.2f} microssegundos")
    else:
        linha = (f"{nome_algoritmo:^10}- "
                f"comparadorado: {comp_info:^7} vez(es) | "
                f"tempo: {timer * 1000000:^7.2f} microssegundos")
    return linha