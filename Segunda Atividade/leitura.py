import sys
import auxiliar

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
        with open(arquivo, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()
            if not linhas:
                print("Arquivo Vazio\n")
                return
            cabecalho_arquivo = linhas[1].strip()
            cabecalho = "key,Name,Alignment,Gender,EyeColor,Race,HairColor,Publisher,SkinColor,Height,Weight,Intelligence,Strength,Speed,Durability,Power,Combat,Total"
            if cabecalho_arquivo != cabecalho:
                auxiliar.reescreverReg(0,0,0,False)
                print("Arquivo Invalido\n")
                return        

        # Chama as funções auxiliares
        sort, order = lerLetras(linhas[0])
        herois = alocarHerois(linhas[2:])  # começa na linha 3
        if sort not in 'qQmMhHiI':
            sort = -1
        if order not in 'cCdD':
            order = -1
        else:
            if order == 'cC':
                order = True
            else:
                order = False

        return herois, sort, order

    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        exit(1)

def alocarHerois(linhas):
    herois = []
    for linha in linhas:
        linha = linha.replace("||", "|-|")  # preenche campos vazios
        atributos = linha.strip().split('|')

        # completa campos faltantes
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
    sort = partes[0].split('=')[1]
    order = partes[1].split('=')[1]
    return sort, order